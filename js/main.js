import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
    {
        'title': "Work Example",
        'href': "https://example.com",
        'desc': "lorem",
        'image': {
            'desc': "example screenshot of a project involving code",
            'scr': "images/example1.png",
            'comment': "",
        }
    },
    {
        'title': "Portfolio Boilerplate",
        'href': "https://example.com",
        'desc': "lorem",
        'image': {
            'desc': "A Serverless Portfolio",
            'scr': "images/example2.png",
            'comment': "",
        }
    },
    {
        'title': "Work Example",
        'href': "https://example.com",
        'desc': "lorem",
        'image': {
            'desc': "example screenshot of a project involving cats",
            'scr': "images/example3.png",
            'comment': "",

        }
    }
]

ReactDom.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'))
