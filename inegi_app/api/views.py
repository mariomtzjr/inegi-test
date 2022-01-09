import os
import requests

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ListEntities(APIView):

    def set_url_parameters(self, kwargs):
        url = os.environ.get('URL_API_BUSQUEDA')
        token = os.environ.get('DENUE_TOKEN_API')
        
        entidad = kwargs.get('ef')
        municipio = kwargs.get('mun')
        establecimiento = kwargs.get('establecimiento')

        localidad = os.environ.get('LOCALIDAD')
        ageb = os.environ.get('AGEB')
        manzana = os.environ.get('MANZANA')
        sector = os.environ.get('SECTOR')
        subsector = os.environ.get('SUBSECTOR')
        rama = os.environ.get('RAMA')
        clase = os.environ.get('CLASE')
        reg_inicial = os.environ.get('REG_INICIAL')
        reg_final = os.environ.get('REG_FINAL')
        id = os.environ.get('ID')

        return f"{url}{entidad}/{municipio}/{localidad}/{ageb}/{manzana}/{sector}/{subsector}/{rama}/{clase}/{establecimiento}/{reg_inicial}/{reg_final}/{id}/{token}"

    def get(self, request, format=None, *args, **kwargs):
        """
        Return list all establishment by state,
        municipality and establishment name

        args:
            ef: state
            mun: municipality
            establecimiento: establishment name
        * Requires token.
        """
 
        urlAPiBusqueda = self.set_url_parameters(kwargs)
        response = requests.get(urlAPiBusqueda).json()

        return Response(response)