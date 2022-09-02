import pendulum
from writer import process_pdf

# User input
input_format = 'DD.MM.YYYY'

# PDF
pdf_number = 'No'
pdf_week_start = 'DD.MM'
pdf_week_end = 'DD.MM.YY'

def validate_format(input):
    try:
        parsed_input = pendulum.from_format(input, input_format)
        return parsed_input
    except ValueError:
        raise ValueError(f"Falsche Eingabe, richtig wäre: {input_format}")

def validate_before(begin_date, end_date):
    if (begin_date > end_date):
        raise ValueError("Der Anfang der Ausbildung kann nicht vor dem Ende liegen!")

started = input('Ausbildung bereits begonnen? (y/n)\n')

if (started == 'y'):
    iteration =  int(input('Welche Nummer trägt dein letzter ausgefüllter Nachweis?\n'))
    begin_date = validate_format(input(f'Gib ein beliebiges Datum in jener Woche an. Wir erstellen dir alle folgenden Nachweise.({input_format})\n')).add(weeks=1)
    end_date = validate_format(input(f'Wann endet deine Ausbildung? ({input_format})\n'))
    validate_before(begin_date, end_date)

    iterations = (begin_date.diff(end_date).in_weeks()+1)

    for i in range(iterations):
        field_dictionary = {
            "Kalenderwoche": begin_date.add(weeks=i).week_of_year,
            "Datum": begin_date.add(weeks=i).start_of('week').format(pdf_week_start) + '-' + begin_date.add(weeks=i).end_of('week').format(pdf_week_end),
            "Seitennummer": i+iteration+1}

        print(field_dictionary)

        process_pdf(f'IHK Berichtsheft {pdf_number}{field_dictionary["Seitennummer"]} {field_dictionary["Datum"]}.pdf', field_dictionary)

elif (started == 'n'):
    begin_date = validate_format(input(f'Wann beginnt deine Ausbildung? ({input_format})\n'))
    end_date = validate_format(input(f'Wann endet deine Ausbildung? ({input_format})\n'))
    validate_before(begin_date, end_date)

    iterations = (begin_date.diff(end_date).in_weeks()+1)

    for i in range(iterations):
        field_dictionary = {
            "Kalenderwoche": begin_date.add(weeks=i).week_of_year,
            "Datum": begin_date.add(weeks=i).start_of('week').format(pdf_week_start) + '-' + begin_date.add(weeks=i).end_of('week').format(pdf_week_end),
            "Seitennummer": i+1}

        print(field_dictionary)

        process_pdf(f'IHK Berichtsheft {pdf_number}{i+1} {field_dictionary["Datum"]}.pdf', field_dictionary)
