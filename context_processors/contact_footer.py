from django.template.context_processors import request

from home.models import HomePage



def contact(request):
        main_model = HomePage.objects.first()
        tel = main_model.home_telephone
        adr = main_model.home_address
        desc = main_model.home_description
        title = main_model.home_title
        

        return {
        "f_tel" : tel,
        "f_adr" : adr,
        "f_desc" : desc,
        "f_title" : title,

        }

