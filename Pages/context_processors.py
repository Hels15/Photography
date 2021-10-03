from .models import PageInfo



def global_context(request):
    page_info_list = PageInfo.objects.all()


    if not page_info_list: #if list index out of range
        return {}

    return {
        "page_title":page_info_list[0].title,
        "subtitle":page_info_list[0].subtitle,
        "email": page_info_list[0].email,
        "phone":page_info_list[0].phone,
        "instagram":page_info_list[0].instagram,
        "facebook":page_info_list[0].facebook,
        "address": page_info_list[0].address
        }