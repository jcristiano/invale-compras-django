from django import template

register = template.Library()

@register.filter()
def addcss(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split(' ')
    if css_classes and arg not in css_classes:
        css_classes.append(arg)
    return value.as_widget(attrs={'class': " ".join(css_classes).strip()})


@register.filter()
def tpddelete(value, arg):
    css_value = 'tpd-manual-pn-control-field-deleted'
    css_classes = value.field.widget.attrs.get('class', '').split(' ')
    if arg == 'D':
        if css_classes and css_value not in css_classes:
            css_classes = '%s %s' % (css_classes, css_value)
    return value.as_widget(attrs={'class': css_classes})


@register.filter(name='attr')
def add_attr(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val

    return field.as_widget(attrs=attrs)