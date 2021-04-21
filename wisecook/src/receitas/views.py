from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.db import connection

from .models import Receita, Utiliza, Recomendada
from possui.models import Possui

@login_required
def recipescreen(request, *args, **kwargs):

    receitas = Receita.objects.filter(nome=kwargs['pk'])
    utiliza = Utiliza.objects.filter(nomereceita=kwargs['pk'])

    obj_dict = {
        'nome':'nome',
        'modopreparo':'modopreparo',
        'ingredientes':[],
    }

    ingredientes = {
    }

    for i in utiliza:
        if str(i.nomereceita) == kwargs['pk']:
            ingredientes[str(i.nomealimento)] = float(i.quantidade)

    for i in range(len(receitas)):
        nome = str(receitas[i].nome)
        modoPreparo = str(receitas[i].modopreparo)
        if nome == kwargs['pk']:
            obj_dict['nome'] = nome
            obj_dict['modopreparo'] = modoPreparo
            obj_dict['ingredientes'] = ingredientes.items()
    
    return render(request,"recipeScreen.html",obj_dict)

@login_required
def feedscreen(request, *args, **kwargs):


    delete_query = "DELETE FROM receitas_recomendada WHERE idusuario_id != 0" 

    insert_query = """
    INSERT INTO receitas_recomendada (nomereceita_id, idusuario_id, correspondencia) (
        SELECT	T.nomereceita_id, %d as Usuario,( CAST(T.quantidadeUsuario AS FLOAT)/ CAST (W.quantidadeReceita AS FLOAT) )*100 as correspondencia
        FROM (	(SELECT 	Z.nomereceita_id,  COUNT(porcentagem) AS quantidadeUsuario
                FROM 	(	SELECT 	X.nomereceita_id, X.nomealimento_id , Y.idUsuario, (Y.quantidade>X.quantidade) AS PORCENTAGEM
                            FROM	(	SELECT	nomereceita_id, nomealimento_id, quantidade
                                        FROM	receitas_utiliza
                                        WHERE 	nomereceita_id IS NOT NULL) X LEFT OUTER JOIN 
                         (	SELECT	U.idusuario, P.nomealimento_id, P.quantidade
                            FROM 	possui_possui P, usuarios_usuario U
                            WHERE 	P.idusuario_id = U.idusuario AND U.idusuario = %d) Y ON X.nomealimento_id = Y.nomeAlimento_id
                        ) Z
                GROUP BY  Z.nomereceita_id) T
                JOIN
                (SELECT nomereceita_id, COUNT(nomealimento_id) as quantidadeReceita
                FROM receitas_utiliza
                GROUP BY nomereceita_id) W
                ON T.nomereceita_id = W.nomereceita_id
            )
        WHERE ( CAST(T.quantidadeUsuario AS FLOAT)/ CAST (W.quantidadeReceita AS FLOAT) )*100 > 25
        ORDER BY correspondencia DESC
    )
    """%(request.user.id, request.user.id)

    cursor = connection.cursor()
    cursor.execute(delete_query)
    
    cursor2 = connection.cursor()
    cursor2.execute(insert_query )
    # cursor2.fetchall()

    utiliza = Utiliza.objects.all()
    possui = Possui.objects.filter(idusuario_id = request.user.id)
    recomendadas = Recomendada.objects.filter(idusuario_id = request.user.id)
    
    return render(request,"novoFeed.html",{'recomendadas':recomendadas, 'possui':possui, 'utiliza':utiliza})