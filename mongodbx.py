#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  mongodbx.py
 #
 #  File Description:
 #      This Python script, mongodbx.py, contains generic Python functions
 #      for completing common tasks with MongoDB databases. 
 #      Here is the list:
 #
 #      insert_dictionary_list_into_collection
 #      insert_json_file_into_collection
 #      delete_records_then_insert_dictionary
 #      return_table_as_dataframe
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  09/18/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import json

import pandas as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'mongodbx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  insert_dictionary_list_into_collection
 #
 #  Function Description:
 #      This function inserts a dictionary or list of dictionaries into a compatible
 #      MongoDB collection.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  pymongo pymongo_collection
 #                          The parameter is the pymongo collection.
 #  list    collection_dictionary_list
 #                          The parameter is the dictionary or dictionary list.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def insert_dictionary_list_into_collection \
        (pymongo_collection,
         collection_dictionary_list):
    
    if isinstance(collection_dictionary_list, list):

        list_length_integer = len(collection_dictionary_list)

        if list_length_integer > 0 and isinstance(collection_dictionary_list[0], dict):

            if list_length_integer > 1:
            
                pymongo_collection.insert_many(collection_dictionary_list)

            elif list_length_integer == 1:

                pymongo_collection.insert_one(collection_dictionary_list[0])
    
    elif isinstance(collection_dictionary_list, dict):
    
        pymongo_collection.insert_one(input_dictionary_list)


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  insert_json_file_into_collection
 #
 #  Function Description:
 #      This function reads the data from a JSON file and populates a MongoDB 
 #      collection with the information.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  pymongo pymongo_collection
 #                          The parameter is the pymongo collection.
 #  string  file_path_string
 #                          The parameter is the file path for the JSON data file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def insert_json_file_into_collection \
        (pymongo_collection,
         file_path_string):
        
    with open(file_path_string) as json_file:
    
        collection_dictionary_list = json.load(json_file)

            
    insert_dictionary_list_into_collection(pymongo_collection, collection_dictionary_list)


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  delete_records_then_insert_dictionary
 #
 #  Function Description:
 #      This function queries based on the query dictionary and deletes any hits 
 #      before inserting the new dictionary into the database.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  pymongo pymongo_collection
 #                          The parameter is the pymongo collection.
 #  dictionary  
 #          query_dictionary
 #                          The parameter is the query critieria for the search.
 #  dictionary  
 #          new_dictionary
 #                          The parameter is the new information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def delete_records_then_insert_dictionary \
        (pymongo_collection,
         query_dictionary,
         new_dictionary):

    if pymongo_collection.find_one(query_dictionary) != None:
    
        documents_count_integer = establishments_pymongo_collection.count_documents(query_dictionary)
    
        if documents_count_integer > 1:
    
            pymongo_collection.delete_many(query_dictionary)
    
        else:
    
            pymongo_collection.delete_one(query_dictionary)
    
    
    pymongo_collection.insert_one(new_dictionary)


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  return_table_as_dataframe
 #
 #  Function Description:
 #      This function queries a table for its contents and returns the results 
 #      as a dataframe.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  pymongo pymongo_collection
 #                          The parameter is the pymongo collection.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_table_as_dataframe(pymongo_collection):

    query_results_dictionary_list = pymongo_collection.find()

    
    temp_dataframe = pd.DataFrame(query_results_dictionary_list)
    
    temp_dataframe.drop(columns = '_id', axis = 1, inplace = True)

    
    return temp_dataframe


# In[ ]:




