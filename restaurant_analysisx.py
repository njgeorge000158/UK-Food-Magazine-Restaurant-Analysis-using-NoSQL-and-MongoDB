#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  restaurant_analysisx.py
 #
 #  File Description:
 #      This Python script, restaurant_analysisx.py, contains generic Python functions
 #      for completing common tasks in the evaluation of restaurant ratings in the
 #      IPython notebook, restaurant_analysis.ipynb. Here is the list:
 #
 #      rearrange_establishments_dataframe_columns
 #      return_geocoordinates
 #      return_restaurant_scores
 #      return_marker_size_series
 #      return_locations_dataframe
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  09/20/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import pandas as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'restaurant_analysisx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  rearrange_establishments_dataframe_columns
 #
 #  Function Description:
 #      This function rearranges the columns for an establishments dataframe 
 #      and returns the new dataframe.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          establishments_dataframe
 #                          The parameter is the input dataframe.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rearrange_establishments_dataframe_columns(establishments_dataframe):

    new_establishments_dataframe \
        = establishments_dataframe  \
            [['_id', 'FHRSID', 'ChangesByServerID', 'LocalAuthorityBusinessID', 'BusinessName',
              'BusinessType', 'BusinessTypeID', 'AddressLine1', 'AddressLine2', 'AddressLine3',
              'AddressLine4', 'PostCode', 'geocode', 'Distance', 'Phone', 'RatingValue',
              'RatingKey', 'RatingDate', 'NewRatingPending', 'scores', 'LocalAuthorityCode',
              'LocalAuthorityName', 'LocalAuthorityWebSite', 'LocalAuthorityEmailAddress',
              'SchemeType', 'RightToReply', 'meta', 'links']]

    return new_establishments_dataframe


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  return_geocoordinates
 #
 #  Function Description:
 #      This function returns the latitude and longitude from a geocode dictionary.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dictionary
 #          input_dictionary
 #                          The parameter is the input geocode dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_geocoordinates(input_dictionary):
    
    latitude_float = input_dictionary['latitude']
    
    longitude_float = input_dictionary['longitude']

    
    return latitude_float, longitude_float


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_restaurant_scores
 #
 #  Function Description:
 #      This function returns the hygiene, structural, and confidence scores
 #      from a scores dictionary for a restaurant.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dictionary
 #          input_dictionary
 #                          The parameter is the input geocode dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_restaurant_scores(input_dictionary):
    
    hygiene_score_integer = input_dictionary['Hygiene']
        
    structural_score_integer = input_dictionary['Structural']
        
    confidence_in_management_score_integer = input_dictionary['ConfidenceInManagement']

    
    return hygiene_score_integer, structural_score_integer, confidence_in_management_score_integer


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  return_marker_size_series
 #
 #  Function Description:
 #      This function returns a series of marker sizes from the product 
 #      of the input series and a multiplicative factor.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input Dictionary.
 #  float   factor_float    The parameter is the multiplicative factor.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_marker_size_series(input_series, factor_float):
    
    return input_series * factor_float


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  return_locations_dataframe
 #
 #  Function Description:
 #      This function returns a dataframe for map display by processing an input dataframe.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          establishments_dataframe
 #                          The parameter is the input dictionary.
 #  string
 #          marker_size_column_string
 #                          The parameter is the column name for calculating marker size.
 #  float   factor_float
 #                          The parameter is the multiplicative factor for calculating 
 #                          marker size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_locations_dataframe \
        (establishments_dataframe,
         marker_size_column_string,
         factor_float = 5.0):
    
    locations_dataframe = establishments_dataframe.copy()

    locations_dataframe[['Latitude', 'Longitude']] \
        = establishments_dataframe['geocode'] \
            .apply(lambda x: pd.Series(return_geocoordinates(x)))

    locations_dataframe[['Hygiene', 'Structural', 'ConfidenceInManagement']] \
        = establishments_dataframe['scores'] \
            .apply(lambda x: pd.Series(return_restaurant_scores(x)))

    locations_dataframe['MarkerSize'] \
        = locations_dataframe[marker_size_column_string] \
            .apply(lambda x: pd.Series(return_marker_size_series(x, factor_float)))

    drop_columns_string_list \
        = ['_id', 'ChangesByServerID', 'FHRSID', 'LocalAuthorityBusinessID',
           'BusinessTypeID', 'Phone', 'Distance', 'RatingKey', 'RightToReply',
           'SchemeType', 'geocode', 'scores', 'LocalAuthorityCode',
           'LocalAuthorityWebSite', 'meta', 'LocalAuthorityEmailAddress', 'links']

    locations_dataframe.drop(drop_columns_string_list, axis = 1, inplace = True)
        
    
    return locations_dataframe


# In[ ]:




