import pandas as pd

from sdv.constraints import create_custom_constraint_class


def is_valid(column_names, data):
    """
    Checks for the validity of the data for the given column names.
    
    Args:
        column_names(list[str]):
            A list of the column names involved in the constraint
        data(pandas.DataFrame):
            A dataaset
        extra_parameters:
            TODO: Add or remove any extra paramters you need

    Returns:
        pandas Series:
            A Series of True/False values describing whether the each row
            of the data is valid. There is exactly 1 True/False value for
            every row in the data.
    """

    validity = [True] * data.shape[0]

    # Extract relevant columns based on provided column names
    day_part_col = column_names[0]
    number_rating_col = column_names[1]
    number_message_received_col = column_names[2]
    number_message_read_col = column_names[3]

    for i, row in data.iterrows():
        day_part_x = row[day_part_col]
        
        if day_part_x == 0:
            if row[number_rating_col] > 1 or row[number_message_received_col] > 1 or row[number_message_read_col] > 1:
                validity[i] = False
        elif day_part_x == 1:
            if row[number_rating_col] > 2 or row[number_message_received_col] > 2 or row[number_message_read_col] > 2:
                validity[i] = False
        elif day_part_x == 2:
            if row[number_rating_col] > 3 or row[number_message_received_col] > 3 or row[number_message_read_col] > 3:
                validity[i] = False

    return pd.Series(validity)

def transform(column_names, data):
    """
    Transforms the data for the given column names. The transformed
    data will be given to the synthetic data model and will ensure that
    the constraint is learned.

    Args:
        column_names(list[str]):
            A list of column names involved in the constraint
        data(pandas.DataFrame):
            A dataset with the original data
        extra_parameters:
            TODO: Add or remove any extra parameters you need

    Returns:
        pandas DataFrame
            The full data after it has been transformed
    """

    # TODO implement your transformation logic
    transformed_data = data
    return transformed_data

def reverse_transform(column_names, transformed_data):
    """
    Reverses the transformation for the column names to recover
    data in the original state. The reverse transform will be applied
    to the synthetic data data the model creates.


    Args:
        column_names(list[str]):
            A list of column names involved in the constraint
        transformed_data(pandas.DataFrame):
            A dataset with the transformed data
        extra_parameters:
            TODO: Add or remove any extra parameters you need

    Returns:
        pandas DataFrame
            The full data after it has been reverse transformed
    """

    # TODO implement your reverse transformation logic
    reversed_data = transformed_data
    return reversed_data

# Create your constraint class
# TODO rename your class to a descriptive name
day_partConstraintClass = create_custom_constraint_class(
    is_valid_fn=is_valid,
    transform_fn=transform, # optional
    reverse_transform_fn=reverse_transform # optional
)

### USE THE CONSTRAINT IN A SEPARATE FILE

# Step 1. Load the constraint
# synthesizer.load_custom_constraint_class(
#     filepath='custom_constraint_template.py'
#     class_names='MyCustomConstraintClass'
# )
   
# Step 2. Apply it
# my_constraint = {
#     'constraint_class': 'MyCustomConstraintClass',
#     'constraint_parameters': {
#         'column_names': [],
#         'extra_parameter': None
#     }
# }
# synthsizer.add_constraints([my_constraint])