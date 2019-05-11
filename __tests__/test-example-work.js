import React from 'react';
import { shallow } from 'enzyme';
import ExampleWork from '../js/example-work';

import Enzyme from 'enzyme':
import Adapter from 'enzyme-adapter-react-16';
Enzyme.configure({ adapter: new Adapter() });

const myWork = [
    {
        'title': "Work Example",
        'image': {
            'desc': "example screenshot of a project involving code",
            'scr': "images/example1.png",
            'comment': "",
        }
    },
    {
        'title': "Portfolio Boilerplate",
        'image': {
            'desc': "A Serverless Portfolio",
            'scr': "images/example2.png",
            'comment': "",
        }
    },
    {
        'title': "Work Example",
        'image': {
            'desc': "example screenshot of a project involving cats",
            'scr': "images/example3.png",
            'comment': "",

        }
    }
];

describe("ExampleWork component", () => {
    let component = shallow<ExampleWork work={myWork}/>;

    let images = component.find("img");

    it("Should be a 'section' element", () => {
        expect(images.length).toEqual(1);
    });

    it("Should contain as many children as there are work examples", () => {
        expect(images.node.props.src).toEqual(myWork[1].image.src);
    });
});
