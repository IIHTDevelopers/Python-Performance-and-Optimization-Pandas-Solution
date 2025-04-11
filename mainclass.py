import pandas as pd
import timeit

class EmployeeDataAnalysis:
    def __init__(self, file_path, data=None):
        """Load CSV data into a Pandas DataFrame."""
        if data:
            self.df = pd.DataFrame(data)
        else:
            self.df = pd.read_csv(file_path)

    def display_head(self):
        """Return the first 5 rows of the DataFrame."""
        return self.df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.df.info()

    def increase_salary_vectorized(self):
        """Increase salary by 10% using vectorized operation."""
        self.df['Salary'] *= 1.10  # More efficient approach
        return self.df

    def increase_salary_loop(self):
        """Increase salary by 10% using a loop."""
        for i in range(len(self.df)):
            self.df.at[i, 'Salary'] = self.df.at[i, 'Salary'] * 1.10
        return self.df

    def compare_performance(self):
        """Compare the performance of vectorized operation vs loop."""
        vectorized_time = timeit.timeit(self.increase_salary_vectorized, number=1)
        loop_time = timeit.timeit(self.increase_salary_loop, number=1)
        return vectorized_time, loop_time

    def save_to_csv(self, output_file="updated_employee_data.csv"):
        """Save the updated DataFrame to a new CSV file."""
        self.df.to_csv(output_file, index=False)
