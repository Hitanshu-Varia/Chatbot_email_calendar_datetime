TOOLS = [
    {
        'type': 'function',
        'function': {
            'name': 'add_two_numbers',
            'description': 'Add two numbers together',
            'parameters': {
                'type': 'object',
                'required': ['a', 'b'],
                'properties': {
                    'a': {
                        'type': 'integer',
                        'description': 'The first number to add'
                    },
                    'b': {
                        'type': 'integer',
                        'description': 'The second number to add'
                    },
                },
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'subtract_two_numbers',
            'description': 'Subtract the second number from the first number',
            'parameters': {
                'type': 'object',
                'required': ['a', 'b'],
                'properties': {
                    'a': {
                        'type': 'integer',
                        'description': 'The number to subtract from',
                    },
                    'b': {
                        'type': 'integer',
                        'description': 'The number to subtract',
                    },
                },
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'multiply_two_numbers',
            'description': 'Multiply two numbers together',
            'parameters': {
                'type': 'object',
                'required': ['a', 'b'],
                'properties': {
                    'a': {
                        'type': 'integer',
                        'description': 'The first number to multiply'
                    },
                    'b': {
                        'type': 'integer',
                        'description': 'The second number to multiply'
                    },
                },
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'divide_two_numbers',
            'description': 'Divide the first number by the second number',
            'parameters': {
                'type': 'object',
                'required': ['a', 'b'],
                'properties': {
                    'a': {
                        'type': 'integer',
                        'description': 'The dividend (number to be divided)'
                    },
                    'b': {
                        'type': 'integer',
                        'description': 'The divisor (number to divide by)'
                    },
                },
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'create_calendar_event',
            'description': 'Create an event in Google Calendar with specified start and end times',
            'parameters': {
                'type': 'object',
                'required': ['summary', 'start_time', 'end_time'],
                'properties': {
                    'summary': {
                        'type': 'string',
                        'description': 'The title/summary of the calendar event'
                    },
                    'start_time': {
                        'type': 'string',
                        'description': 'Start time in ISO format (e.g., 2025-06-13T16:00:00+05:30)'
                    },
                    'end_time': {
                        'type': 'string',
                        'description': 'End time in ISO format (e.g., 2025-06-13T17:00:00+05:30)'
                    },
                },
            },
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'send_email',
            'description': 'Send an email using Gmail to a specified recipient',
            'parameters': {
                'type': 'object',
                'required': ['to', 'subject', 'message'],
                'properties': {
                    'to': {
                        'type': 'string',
                        'description': 'Email address of the recipient'
                    },
                    'subject': {
                        'type': 'string',
                        'description': 'Subject line of the email'
                    },
                    'message': {
                        'type': 'string',
                        'description': 'Body content of the email'
                    },
                },
            },
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'get_current_time',
            'description': 'Get the current date and time',
            'parameters': {
                'type': 'object',
                'properties': {},
                'required': []
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'fallback',
            'description': 'Use this when no other tool fits the user query. Provides general conversational responses.',
            'parameters': {
                'type': 'object',
                'required': ['message'],
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'The user query or message to respond to',
                    },
                },
            },
        },
    }
]