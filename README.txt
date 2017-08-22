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
			 - Doivent être téléchargés à partir de : http://10.4.247.72:8888/impala/#query
			 - Executer une requête de la sorte: 		
									1 SELECT * FROM voice
									2 WHERE voice.date_utc_agent BETWEEN '2017-06-01 00:00:00' AND '2017-06-02 00:00:00'
									3 order by voice.date_utc_agent desc
			 - Il ne reste plus qu'à modifier les dates des requêtes.

			 - Aprés téléchargement le fichier VOIX doit être renommé sous: "VOIX.csv"                                           <-- **IMPORTANT!!!**
			 - Il doit y avoir dans le même directory également une extraction d'océan renommée sous: "g2r.csv"                  <-- **IMPORTANT!!!**



	#DASHBOARD DATA: 
		Les fichiers DATA:
			 - Doivent être téléchargés à partir de : http://10.4.247.72:8888/impala/#query
			 

		  __FICHIER HTTP__:



				- Executer une requête de la sorte: 			
										1  SELECT * FROM data_http
										2  WHERE data_http.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by data_http.date_utc_agent desc    
			- Il ne reste plus qu'à modifier les dates des requêtes.

			- Aprés téléchargement le fichier HTTP doit être renommé sous: "HTTP.csv"                                           <-- **IMPORTANT!!!**
			

		   __FICHIER WEB__:



				- Executer une requête de la sorte: 			
										1  SELECT * FROM web
										2  WHERE web.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by web.date_utc_agent desc    
			- Il ne reste plus qu'à modifier les dates des requêtes.

			- Aprés téléchargement le fichier HTTP doit être renommé sous: "WEB.csv"                                           <-- **IMPORTANT!!!**



		   __FICHIER VIDEO__:



				- Executer une requête de la sorte: 			
										1  SELECT * FROM video_streaming
										2  WHERE video_streaming.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by video_streaming.date_utc_agent desc   
			- Il ne reste plus qu'à modifier les dates des requêtes.

			- Aprés téléchargement le fichier HTTP doit être renommé sous: "VIDEO.csv"                                           <-- **IMPORTANT!!!**
			
			
		   __FICHIER USAGES__:



				- Executer une requête de la sorte: 			
										1  SELECT * FROM application_volume
										2  WHERE application_volume.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by application_volume.date_utc_agent desc
			- Il ne reste plus qu'à modifier les dates des requêtes.

			- Aprés téléchargement le fichier HTTP doit être renommé sous: "APPLICATION.csv"                                    <-- **IMPORTANT!!!**



		  ##IMPORTANT!!!:
				Dans le même Directory que tout les fichiers DATA il doit y avoir:

				- Une extraction d'océan renommée sous: "g2r.csv"                  					    						<-- **IMPORTANT!!!**
				
				A l'execution du dashboard il est nécéssaire de séléctionner un fichier "HTTP.CSV" uniquement!!!				<-- **IMPORTANT!!!**
				
				
____________________________________________________________________________________________________________________________________________________________
------------------------------------------------------*****INVESTIGATION*****-------------------------------------------------------------------------------
____________________________________________________________________________________________________________________________________________________________
				
#INVESTIGATION
	#INVESTIGATION VOIX:
		Les fichiers VOIX:
			 - Doivent être téléchargés à partir de : http://10.4.247.72:8888/impala/#query
			 - Executer une requête de la sorte: 		
									1 SELECT * FROM voice
									2 WHERE voice.date_utc_agent BETWEEN '2017-06-01 00:00:00' AND '2017-06-02 00:00:00'
									3 order by voice.date_utc_agent desc
			 - Il ne reste plus qu'à modifier les dates des requêtes.

			 - Aprés téléchargement le fichier VOIX doit être renommé sous: "VOIX.csv"                                           <-- **IMPORTANT!!!**
			 - Il doit y avoir dans le même directory également une extraction d'océan renommée sous: "g2r.csv"                  <-- **IMPORTANT!!!**
			 
			 
	#INVESTIGATION DATA:
	
		__FICHIER HTTP__:



			- Executer une requête de la sorte: 			
										1  SELECT * FROM data_http
										2  WHERE data_http.date_utc_agent BETWEEN '2017-01-01 00:00:00' AND '2017-04-07 00:00:00'
										3  order by data_http.date_utc_agent desc    
			- Il ne reste plus qu'à modifier les dates des requêtes.

			- Aprés téléchargement le fichier HTTP doit être renommé sous: "HTTP.csv"                                           <-- **IMPORTANT!!!**
			
			- Il doit y avoir dans le même directory également une extraction d'océan renommée sous: "g2r.csv"                  <-- **IMPORTANT!!!**
			
			
			#IMPORTANT!:
				DANS Investigation DATA on n'a besoin que du fichier HTTP avec la bonne nomination
