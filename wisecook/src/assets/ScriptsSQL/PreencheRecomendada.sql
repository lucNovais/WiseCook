DELETE * FROM RECOMENDADA;

INSERT INTO RECOMENDADA (nomeReceita, usuario, correspondencia) (
	SELECT	T.nomeReceita, 2 as Usuario,( CAST(T.quantidadeUsuario AS FLOAT)/ CAST (W.quantidadeReceita AS FLOAT) )*100 as correspondencia
	FROM (	(SELECT 	z.nomeReceita,  COUNT(porcentagem) AS quantidadeUsuario
			FROM 	(	SELECT 	X.nomeReceita, X.nomeAlimento , Y.idUsuario, (Y.quantidade>X.quantidade) AS PORCENTAGEM
						FROM	(	SELECT	nomeReceita, nomeAlimento, quantidade
									FROM	UTILIZA
									WHERE 	nomeReceita IS NOT NULL) X LEFT OUTER JOIN 
					(	SELECT	U.idUsuario, P.nomeAlimento, P.quantidade
						FROM 	POSSUI P, USUARIO U
						WHERE 	P.usuario = U.idUsuario AND U.idUsuario = 2) Y ON X.nomeAlimento = Y.nomeAlimento
					) Z
			GROUP BY  Z.nomeReceita) T
			JOIN
			(SELECT nomeReceita, COUNT(nomeAlimento) as quantidadeReceita
			FROM UTILIZA
			GROUP BY nomeReceita) W
			ON T.nomeReceita = W.nomeReceita
		)
);