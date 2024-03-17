import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = None

  # ¿Cuántos de cada raza están representados en este conjunto de datos? Esta debería ser una serie de Pandas con nombres de raza como etiquetas de índice.
    race_count = df['race'].value_counts()

    # ¿Cuál es la edad promedio de los hombres?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # ¿Cuál es el porcentaje de personas que tienen una licenciatura?
    licenciatura = df[df['education'] == 'Bachelors'].shape[0]
    total_personas = df.shape[0]
    percentage_bachelors = (licenciatura / total_personas) * 100

    #¿Qué porcentaje de personas con educación avanzada ("licenciatura", "maestría" o "doctorado") ganan más de 50.000 dólares?
    # ¿Qué porcentaje de personas sin educación avanzada ganan más de 50.000 dólares?

    # con y sin `Licenciatura`, `Maestría` o `Doctorado`
    bachelors = df[ df['education'] == 'Bachelors']
    bachelors_salary = bachelors[bachelors['salary'] == '<=50K'].shape[0]
    total_personas = df.shape[0]
    porcentaje_bachelors = (bachelors_salary / total_personas) * 100

    master = df[ df['education'] == 'Masters']
    master_salary = master[master['salary'] == '<=50K'].shape[0]
    total_personas = df.shape[0]
    porcentaje_master = (master_salary / total_personas) * 100

    doctorate = df[ df['education'] == 'Doctorate']
    doctorate_salary = doctorate[doctorate['salary'] == '<=50K'].shape[0]
    total_personas = df.shape[0]
    porcentaje_doctorate = (doctorate_salary / total_personas) * 100
 

    # Filtrar personas sin educación avanzada
    sin_educacion = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    # Contar personas sin educación avanzada que ganan más de $50,000
    num_sin_educacion = sin_educacion[sin_educacion['salary'] == '<=50K'].shape[0]
    # Calcular el total de personas sin educación avanzada
    total_sin_educacion_avanzada = sin_educacion.shape[0]
    # Calcular el porcentaje de personas sin educación avanzada que ganan más de $50,000
    porcentaje_sin_educacion_avanzada_mas_50000 = (num_sin_educacion / total_sin_educacion_avanzada) * 100

    # percentage with salary >50K
    higher_education_rich = [porcentaje_bachelors, porcentaje_master, porcentaje_doctorate]
    lower_education_rich = porcentaje_sin_educacion_avanzada_mas_50000

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    # Encontrar el número mínimo de horas por semana
    min_hours_per_week = df['hours-per-week'].min()

    # Filtrar personas que trabajan el número mínimo de horas por semana
    personas_min_hours_per_week = df[df['hours-per-week'] == min_hours_per_week]

    # Contar personas que trabajan el número mínimo de horas por semana y tienen un salario > $50,000
    personas_min_hours_per_week_salario_mas_50k = personas_min_hours_per_week[personas_min_hours_per_week['salary'] == '<=50K'].shape[0]

    # Calcular el total de personas que trabajan el número mínimo de horas por semana
    num_min_workers = personas_min_hours_per_week.shape[0]

    # Calcular el porcentaje de personas que trabajan el número mínimo de horas por semana y tienen un salario > $50,000
    rich_percentage = (personas_min_hours_per_week_salario_mas_50k / num_min_workers) * 100
    

    # What country has the highest percentage of people that earn >50K?
    # Obtener el total de personas en cada país
    total_personas_por_pais = df['native-country'].value_counts()

    # Obtener el total de personas en cada país que ganan más de $50,000
    total_personas_mas_50k_por_pais = df[df['salary'] == '<=50K']['native-country'].value_counts()

    # Calcular el porcentaje de personas en cada país que ganan más de $50,000
    porcentaje_mas_50k_por_pais = (total_personas_mas_50k_por_pais / total_personas_por_pais) * 100

    # Encontrar el país con el mayor porcentaje de personas que ganan más de $50,000
    pais_mayor_porcentaje = porcentaje_mas_50k_por_pais.idxmax()
    mayor_porcentaje = porcentaje_mas_50k_por_pais.max()
    
    highest_earning_country = pais_mayor_porcentaje
    highest_earning_country_percentage = mayor_porcentaje

    # Identify the most popular occupation for those who earn >50K in India.

    # Filtrar personas de India que ganan más de $50,000
    india_mas_50k = df[(df['native-country'] == 'India') & (df['salary'] == '<=50K')]

    # Identificar la ocupación más popular
    top_IN_occupation = india_mas_50k['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
