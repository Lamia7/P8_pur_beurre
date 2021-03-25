from search.forms import NavSearchForm


def navigation_search_form(request):
    nav_search_form = NavSearchForm()  # instanciate form
    context = {
        "nav_search_form": nav_search_form,  # key: variables we access from template
    }

    return context
