from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .constants import INDEX_TEMPLATE, NON_UNIQUE_CUSTOMID_MSG
from .forms import URLForm
from .models import URLMap
from .services import get_unique_short_id


@app.route("/", methods=["GET", "POST"])
def index_view():
    """Главная страница с формой сокращения ссылок."""
    form = URLForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id:
            if URLMap.query.filter_by(short=custom_id).first() is not None:
                flash(NON_UNIQUE_CUSTOMID_MSG % custom_id)
                return render_template(INDEX_TEMPLATE, form=form)
        else:
            custom_id = get_unique_short_id()
        url_object = URLMap(original=form.original_link.data, short=custom_id)
        db.session.add(url_object)
        db.session.commit()
        flash("Ваша новая ссылка готова: ")
        return render_template(
            INDEX_TEMPLATE,
            form=form,
            new_url=url_for(
                "redirect_view", short_id=url_object.short, _external=True
            ),
        )
    return render_template(INDEX_TEMPLATE, form=form)


@app.route("/<string:short_id>")
def redirect_view(short_id):
    """Переадресация сокращенных ссылок."""
    url_relation = URLMap.query.filter_by(short=short_id).first()
    if url_relation is None:
        abort(404)
    return redirect(url_relation.original)
