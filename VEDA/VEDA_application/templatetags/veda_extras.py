from django import template

register = template.Library()

@register.simple_tag
def get_avg_user(notes, user):
    count = 0
    sum = 0

    for note in notes:
        if note.receiver == user:
            try:
                sum += int(note.value)
                count += 1
            except:
                pass
    
    return sum / count if count > 0 else 0


@register.simple_tag
def get_avg_user_month(notes, user, month):
    count = 0
    sum = 0

    for note in notes:
        if note.receiver == user and note.date_of_receive.month == month:
            try:
                sum += int(note.value)
                count += 1
            except:
                pass
    
    return sum / count if count > 0 else 0


@register.simple_tag
def get_avg_user_month_discipline(notes, user, month, discipline ):
    count = 0
    sum = 0

    for note in notes:
        if note.receiver == user and note.date_of_receive.month == month and note.discipline == discipline:
            try:
                sum += int(note.value)
                count += 1
            except:
                pass
    
    return sum / count if count > 0 else 0


@register.simple_tag
def get_count_n_user(notes, user):
    count = 0

    for note in notes:
        if note.receiver == user and note.value == "н":
            count += 1
    
    return count


@register.simple_tag
def get_count_n_user_month(notes, user, month):
    count = 0

    for note in notes:
        if note.receiver == user and note.value == "н" and note.date_of_receive.month == month:
            count += 1
    
    return count


@register.simple_tag
def get_count_n_user_month_discipline(notes, user, month, discipline):
    count = 0

    for note in notes:
        if note.receiver == user and note.value == "н" and note.date_of_receive.month == month and note.discipline == discipline:
            count += 1
    
    return count


@register.simple_tag
def get_count_n(notes):
    count = 0

    for note in notes:
        if note.value == "н" :
            count += 1
    
    return count


@register.simple_tag
def get_count_n_month(notes, month):
    count = 0

    for note in notes:
        if note.value == "н" and note.date_of_receive.month == month:
            count += 1
    
    return count



@register.simple_tag
def get_count_n_month_discipline(notes, month, discipline):
    count = 0

    for note in notes:
        if note.value == "н" and note.date_of_receive.month == month and note.discipline == discipline:
            count += 1
    
    return count


@register.simple_tag
def get_count_neud(notes):
    count = 0

    for note in notes:
        try:
            if int(note.value) < 4 :
                count += 1
        except:
            pass
    
    return count


@register.simple_tag
def get_count_neud_month(notes, month):
    count = 0

    for note in notes:
        try:
            if int(note.value) < 4 and note.date_of_receive.month == month:
                count += 1
        except:
            pass
    
    return count



@register.simple_tag
def get_count_neud_month_discipline(notes, month, discipline):
    count = 0

    for note in notes:
        try:
            if int(note.value) < 4 and note.date_of_receive.month == month and note.discipline == discipline:
                count += 1
        except:
            pass
    
    return count



@register.simple_tag
def get_avg(notes):
    count = 0
    sum = 0

    for note in notes:
        try:
            sum += int(note.value)
            count += 1
        except:
            pass
    
    return sum / count if count > 0 else 0


@register.simple_tag
def get_avg_month(notes, month):
    count = 0
    sum = 0

    for note in notes:
        if note.date_of_receive.month == month:
            try:
                sum += int(note.value)
                count += 1
            except:
                pass
    
    return sum / count if count > 0 else 0


@register.simple_tag
def get_avg_month_discipline(notes, month, discipline ):
    count = 0
    sum = 0

    for note in notes:
        if note.date_of_receive.month == month and note.discipline == discipline:
            try:
                sum += int(note.value)
                count += 1
            except:
                pass
    
    return sum / count if count > 0 else 0