from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime


#   -----------------------------------
#   TABLE PROF 
#   -----------------------------------

class Prof(SQLModel,table=True):
    id_prof : int |None = Field(default=None,primary_key=True)
    nom : str 
    prenom : str 

#   -----------------------------------
#   TABLE PROMOTION  
#   -----------------------------------

class Promotion(SQLModel,table=True):
    id_promo : int |None = Field(default=None,primary_key=True)
    nom_promotion : str 
    annee : int 

#   -----------------------------------
#   TABLE USER 
#   -----------------------------------

class User(SQLModel,table=True):
    id_user : int |None = Field(default=None,primary_key=True)
    email : str 
    password : str 
    admin : bool 

#   -----------------------------------
#   TABLE SALLE  
#   -----------------------------------    

class Salle(SQLModel,table=True):
    id_salle : int | None = Field(default=None,primary_key=True)
    nom_salle : str 
    capacite : int 

#   -----------------------------------
#   TABLE COURS   
#   -----------------------------------  

class Cours(SQLModel,table=True):
    id_cours : int | None = Field(default=None,primary_key=True)
    matiere : str 
    date_debut : datetime 
    date_fin : datetime
    duree_total : datetime 
    id_promo : int | None = Field(default=None,foreign_key="promotion.id_promo")
    id_salle : int | None = Field(default=None,foreign_key="salle.id_salle")
    id_prof : int | None = Field(default=None,foreign_key="prof.id_prof")
    
