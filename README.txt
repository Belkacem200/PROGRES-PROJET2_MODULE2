----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------***SFR DATA ANALYSER***---------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------HELLO-------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

____________________________________________________________________________________________________________________________________________________________
----------------------------------------------------------*****DASHBOARD*****-------------------------------------------------------------------------------
____________________________________________________________________________________________________________________________________________________________

#DASHBOARDS:
	
	#DASHBOARD VOIX:
		Les fichiers VOIX:
			 - Doivent �tre t�l�charg�s � partir de : http://10.4.247.72:8888/impala/#query
			 - Executer une requ�te de la sorte: 		
									1 SELECT * FROM voice
									2 WHERE voice.date_utc_agent BETWEEN '2017-06-01 00:00:00' AND '2017-06-02 00:00:00'
									3 order by voice.date_utc_agent desc
			 - Il ne reste plus qu'� modifier les dates des requ�tes.

			 - Apr�s t�l�chargement le fichier VOIX doit �tre renomm� sous: "VOIX.csv"                                           <-- **IMPORTANT!!!**
			 - Il doit y avoir dans le m�me directory �galement une extraction d'oc�an renomm�e sous: "g2r.csv"                  <-- **IMPORTANT!!!**



	#DASHBOARD DATA: 
		Les fichiers DATA:
			 - Doivent �tre t�l�charg�s � partir de : http://10.4.247.72:8888/impala/#query
			 

		  __FICHIER HTTP__:



				- Executer une requ�te de la sorte: 			
										1  SELECT * FROM data_http
										2  WHERE data_http.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by data_http.date_utc_agent desc    
			- Il ne reste plus qu'� modifier les dates des requ�tes.

			- Apr�s t�l�chargement le fichier HTTP doit �tre renomm� sous: "HTTP.csv"                                           <-- **IMPORTANT!!!**
			

		   __FICHIER WEB__:



				- Executer une requ�te de la sorte: 			
										1  SELECT * FROM web
										2  WHERE web.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by web.date_utc_agent desc    
			- Il ne reste plus qu'� modifier les dates des requ�tes.

			- Apr�s t�l�chargement le fichier HTTP doit �tre renomm� sous: "WEB.csv"                                           <-- **IMPORTANT!!!**



		   __FICHIER VIDEO__:



				- Executer une requ�te de la sorte: 			
										1  SELECT * FROM video_streaming
										2  WHERE video_streaming.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by video_streaming.date_utc_agent desc   
			- Il ne reste plus qu'� modifier les dates des requ�tes.

			- Apr�s t�l�chargement le fichier HTTP doit �tre renomm� sous: "VIDEO.csv"                                           <-- **IMPORTANT!!!**
			
			
		   __FICHIER USAGES__:



				- Executer une requ�te de la sorte: 			
										1  SELECT * FROM application_volume
										2  WHERE application_volume.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by application_volume.date_utc_agent desc
			- Il ne reste plus qu'� modifier les dates des requ�tes.

			- Apr�s t�l�chargement le fichier HTTP doit �tre renomm� sous: "APPLICATION.csv"                                    <-- **IMPORTANT!!!**



		  ##IMPORTANT!!!:
				Dans le m�me Directory que tout les fichiers DATA il doit y avoir:

				- Une extraction d'oc�an renomm�e sous: "g2r.csv"                  					    						<-- **IMPORTANT!!!**
				
				A l'execution du dashboard il est n�c�ssaire de s�l�ctionner un fichier "HTTP.CSV" uniquement!!!				<-- **IMPORTANT!!!**
				
				
____________________________________________________________________________________________________________________________________________________________
------------------------------------------------------*****INVESTIGATION*****-------------------------------------------------------------------------------
____________________________________________________________________________________________________________________________________________________________
				
#INVESTIGATION
	#INVESTIGATION VOIX:
		Les fichiers VOIX:
			 - Doivent �tre t�l�charg�s � partir de : http://10.4.247.72:8888/impala/#query
			 - Executer une requ�te de la sorte: 		
									1 SELECT * FROM voice
									2 WHERE voice.date_utc_agent BETWEEN '2017-06-01 00:00:00' AND '2017-06-02 00:00:00'
									3 order by voice.date_utc_agent desc
			 - Il ne reste plus qu'� modifier les dates des requ�tes.

			 - Apr�s t�l�chargement le fichier VOIX doit �tre renomm� sous: "VOIX.csv"                                           <-- **IMPORTANT!!!**
			 - Il doit y avoir dans le m�me directory �galement une extraction d'oc�an renomm�e sous: "g2r.csv"                  <-- **IMPORTANT!!!**
			 
			 
	#INVESTIGATION DATA:
	
		__FICHIER HTTP__:



			- Executer une requ�te de la sorte: 			
										1  SELECT * FROM data_http
										2  WHERE data_http.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by data_http.date_utc_agent desc    
			- Il ne reste plus qu'� modifier les dates des requ�tes.

			- Apr�s t�l�chargement le fichier HTTP doit �tre renomm� sous: "HTTP.csv"                                           <-- **IMPORTANT!!!**
			
			- Il doit y avoir dans le m�me directory �galement une extraction d'oc�an renomm�e sous: "g2r.csv"                  <-- **IMPORTANT!!!**
			
			
			#IMPORTANT!:
				DANS Investigation DATA on n'a besoin que du fichier HTTP avec la bonne nomination
