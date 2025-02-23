import pandas as pd

def calculate_demographic_data(print_data=True):
   data = pd.read_csv('adult.data.csv')
   data_frame = pd.DataFrame(data)
   d_race = data['race'].value_counts()

   avg_men = round(data.loc[data['sex'] == 'Male','age'].mean(),1)

   bach_degre_n = data['education'].loc[data['education'] == 'Bachelors'].count()
   bach_degre_d = data['education'].count()
   bach_degre_p = round((bach_degre_n / bach_degre_d) * 100,1)

   bach_degre_rich = data_frame.loc[((data_frame['education'] == 'Bachelors') | (data_frame['education'] == 'Masters') | (data_frame['education'] == 'Doctorate')) & (data_frame['salary'] == '>50K')].shape[0]
   bach_degre_d_high = data_frame[(data_frame['education'] == 'Bachelors') | (data_frame['education'] == 'Masters') | (data_frame['education'] == 'Doctorate')].shape[0]
   higher_education_rich = round((bach_degre_rich / bach_degre_d_high) * 100,1)

   low_degre_rich = data_frame.loc[((data_frame['education'] != 'Bachelors') & (data_frame['education'] != 'Masters') & (data_frame['education'] != 'Doctorate')) & (data_frame['salary'] == '>50K')].shape[0]
   bach_degre_d_low = data_frame[(data_frame['education'] != 'Bachelors') & (data_frame['education'] != 'Masters') & (data_frame['education'] != 'Doctorate')].shape[0]
   lower_education_rich = round((low_degre_rich / bach_degre_d_low) * 100,1)

   min_work_hours = data_frame['hours-per-week'].min()
   
   bach_degre_d_min = data_frame[data_frame['hours-per-week'] == min_work_hours].shape[0]
   rich_percentage_num = data_frame.loc[(data_frame['hours-per-week'] == min_work_hours) & (data_frame['salary'] == '>50K')].shape[0]
   rich_percentage = round((rich_percentage_num / bach_degre_d_min) * 100,1)
   
   highest_earning_country_de = data_frame['native-country'].value_counts()
   highest_earning_country_num = data_frame['native-country'][data_frame['salary'] == '>50K'].value_counts()
   highest_earning_country_p = round((highest_earning_country_num / highest_earning_country_de) * 100,1)
   highest_earning_country = highest_earning_country_p.idxmax()
   highest_earning_country_percentage = highest_earning_country_p.max()

   top_IN_occupation = (data_frame['occupation'][(data_frame['native-country'] == 'India') & (data_frame['salary'] == '>50K')].value_counts()).idxmax()

   return {
      'race_count': d_race,
      'average_age_men': avg_men,
      'percentage_bachelors': bach_degre_p,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
     }