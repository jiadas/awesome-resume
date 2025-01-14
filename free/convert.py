import pdfkit
options = {
    'page-size': 'A4',
    'margin-top': '0.05in',
    'margin-right': '0.75in',
    'margin-bottom': '0.05in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}

pdfkit.from_file('free_resume.html', 'resume.pdf', options=options)
