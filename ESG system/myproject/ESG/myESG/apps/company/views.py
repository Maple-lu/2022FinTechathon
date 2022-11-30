from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse

import time

from company.models import Company,Company_E,Category,Company_S,Company_G,City

from .forms import CompanyPostForm#CompanyPost_1Form,CompanyPost_2Form,CompanyPost_3Form
# Create your views here.


class CompanyView(View):
    def get(self,request,*args, **kwargs):
        #从数据库获取数据
        all_companys = Company.objects.all()
        companys_nums = Company.objects.count()
        return render(request, "company.html",{
            "all_companys":all_companys,
            "company_nums":companys_nums,
            })


class CompanyPostView(View):
    def get(self, request, *args, **kwargs):
        all_Categorys = Category.objects.all()
        all_City = City.objects.all()
        return render(request,"servers.html",{
            "all_Categorys": all_Categorys,
            "all_City":all_City
        })

    def post(self, request, *args, **kwargs):
        company_post_form = CompanyPostForm(request.POST)
        if company_post_form.is_valid():
            name = company_post_form.cleaned_data["name"]
            category = request.POST.get('category')
            city = request.POST.get('city')
            new_name = name
            new_category = Category.objects.get(name = category)
            new_city = City.objects.get(name=city)
            Company.objects.get_or_create(name=new_name,category =new_category,city=new_city)

            return HttpResponseRedirect(reverse("servers_1"))
        else:
                # 查询到公司
                return HttpResponseRedirect(reverse("servers_1"))


class ShowView(View):
    def get(self, request, *args, **kwargs):
        all_companys = Company.objects.all()
        companys_nums = Company.objects.count()
        companys_e = Company_E.objects.all()
        return render(request, "datashow.html",{
            "all_companys":all_companys,
            "company_nums":companys_nums,
            "companys_e":companys_e
            })


class CompanyPost_1View(View):
    def get(self, request, *args, **kwargs):
        all_companys = Company.objects.all()
        all_Categorys = Category.objects.all()
        return render(request,"servers_1.html",{
            "all_companys": all_companys,
            "all_Categorys": all_Categorys,
        })

    def post(self, request, *args, **kwargs):
            name = request.POST.get("name")
            category = request.POST.get('category')
            date = request.POST.get("date")
            water_consumption = request.POST.get("water_consumption")
            Energy_consumption = request.POST.get("Energy_consumption")
            Greenhouse_gas_emissions = request.POST.get("Greenhouse_gas_emissions")
            Environmental_protection_action_investment = request.POST.get("Environmental_protection_action_investment")
            save_coal = request.POST.get("save_coal")
            cut_co2 = request.POST.get("cut_co2")
            cut_COD = request.POST.get("cut_COD")
            cut_andan = request.POST.get("cut_andan")
            cut_water = request.POST.get("cut_water")
            oil_waste = request.POST.get("oil_waste")
            paper_waste = request.POST.get("paper_waste")
            cut_so2 = request.POST.get("cut_so2")
            cut_NO = request.POST.get("cut_NO")


            company = Company.objects.get(name = name)
            e_name = Category.objects.get(name = category)
            e_date = date
            Company_E.objects.get_or_create(company=company,name =e_name,date=e_date,water_consumption=water_consumption,Energy_consumption=Energy_consumption,Greenhouse_gas_emissions=Greenhouse_gas_emissions,
                                            Environmental_protection_action_investment=Environmental_protection_action_investment,
                                            save_coal=save_coal,cut_COD=cut_COD,cut_co2=cut_co2,cut_water=cut_water,cut_andan=cut_andan,oil_waste=oil_waste,paper_waste=paper_waste,
                                            cut_NO=cut_NO,cut_so2=cut_so2)

            return HttpResponseRedirect(reverse("servers_2"))


class CompanyPost_2View(View):
    def get(self, request, *args, **kwargs):
        all_companys = Company.objects.all()
        all_Categorys = Category.objects.all()
        return render(request, "servers_2.html", {
            "all_companys": all_companys,
            "all_Categorys": all_Categorys,
        })

    def post(self, request, *args, **kwargs):
            name = request.POST.get("name")
            category = request.POST.get('category')
            date = request.POST.get("date")
            puhui = request.POST.get("puhui")
            gupiao = request.POST.get("gupiao")
            workers = request.POST.get("workers")
            female = request.POST.get("female")
            shenong = request.POST.get("shenong")
            donate = request.POST.get("donate")

            company = Company.objects.get(name = name)
            e_name = Category.objects.get(name = category)
            e_date = date
            Company_S.objects.get_or_create(company=company,name =e_name,date=e_date,puhui=puhui,gupiao=gupiao,workers=workers,female=female,shenong=shenong,donate=donate)

            return HttpResponseRedirect(reverse("servers_3"))


class CompanyPost_3View(View):
    def get(self, request, *args, **kwargs):
        all_companys = Company.objects.all()
        all_Categorys = Category.objects.all()
        return render(request,"servers_3.html",{
            "all_companys": all_companys,
            "all_Categorys": all_Categorys,
        })

    def post(self, request, *args, **kwargs):

            name = request.POST.get("name")
            category = request.POST.get('category')
            date = request.POST.get("date")
            value = request.POST.get("value")
            pure_value = request.POST.get("pure_value")
            tax = request.POST.get("tax")

            company = Company.objects.get(name = name)
            e_name = Category.objects.get(name = category)
            e_date = date
            Company_G.objects.get_or_create(company=company,name =e_name,date=e_date,value=value,pure_value=pure_value,tax=tax)

            return HttpResponseRedirect(reverse("index"))


class CompanyPost_preView(View):
    def get(self, request, *args, **kwargs):
        return render(request,"servers_predict.html")

    def post(self, request, *args, **kwargs):
            water_consumption = request.POST.get("water_consumption")
            Energy_consumption = request.POST.get("Energy_consumption")
            Greenhouse_gas_emissions = request.POST.get("Greenhouse_gas_emissions")
            Environmental_protection_action_investment = request.POST.get("Environmental_protection_action_investment")
            save_coal = request.POST.get("save_coal")
            cut_co2 = request.POST.get("cut_co2")
            cut_COD = request.POST.get("cut_COD")
            cut_andan = request.POST.get("cut_andan")
            cut_water = request.POST.get("cut_water")
            oil_waste = request.POST.get("oil_waste")
            paper_waste = request.POST.get("paper_waste")
            cut_so2 = request.POST.get("cut_so2")
            cut_NO = request.POST.get("cut_NO")
            puhui = request.POST.get("puhui")
            gupiao = request.POST.get("gupiao")
            workers = request.POST.get("workers")
            female = request.POST.get("female")
            shenong = request.POST.get("shenong")
            donate = request.POST.get("donate")
            value = request.POST.get("value")
            pure_value = request.POST.get("pure_value")
            tax = request.POST.get("tax")
            time.sleep(8)
            return HttpResponseRedirect(reverse("grade"))


class grade(View):
    def get(self, request, *args, **kwargs):
        return render(request,"grade.html")


class Company_detailView(View):
    def get(self,request,*args, **kwargs):
        #从数据库获取数据
        name = request.GET.get('id')
        company = Company.objects.get(id=name)
        company_e = Company_E.objects.filter(company_id=name)
        all_companys = Company.objects.all()
        return render(request, "company-detail.html",{
            "all_companys":all_companys,
            "all_company_e":company_e,
            "company":company
            })


class Company_detailView1(View):
    def get(self,request,*args, **kwargs):
        #从数据库获取数据
        name = request.GET.get('id')
        company = Company.objects.get(id=name)
        company_s = Company_S.objects.filter(company_id=name)
        all_companys = Company.objects.all()
        return render(request, "company-detail1.html",{
            "all_companys":all_companys,
            "all_company_s":company_s,
            "company":company
            })


class Company_detailView2(View):
    def get(self,request,*args, **kwargs):
        #从数据库获取数据
        name = request.GET.get('id')
        company = Company.objects.get(id=name)
        company_g = Company_G.objects.filter(company_id=name)
        all_companys = Company.objects.all()
        return render(request, "company-detail2.html",{
            "all_companys":all_companys,
            "all_company_g":company_g,
            "company":company
            })