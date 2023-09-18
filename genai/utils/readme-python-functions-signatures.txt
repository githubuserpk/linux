def clean_missing_numerics(df: pd.DataFrame, numeric_columns): 
  text1 code
  text2 code


def data_selection(df: pd.DataFrame, selected_columns: List[str], label_column: str) -> (pd.DataFrame, pd.Series):
  text1 code
  text2 code

  return data, labels


def train_pipeline(clf: Pipeline, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.DataFrame, np.ndarray]) -> float:
  text1 code
  ....
  return score


def process_gcs_uri(uri:str) -> (str,str,str,str):
'''
#Note: receives a GCS uril and breaks it down to the scheme, bucket, path and file
Parameters: 
  uri (str): GCS uri

Returns:
  scheme(str): uri scheme
  bucket(str): uri bucket
  path(str): uri path
  file(str): uri file
'''

