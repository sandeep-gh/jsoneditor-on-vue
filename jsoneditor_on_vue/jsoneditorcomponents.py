import demjson3 as demjson
from addict import Dict
import justpy as jp
from justpy import JustpyBaseComponent
from justpy import WebPage
from tailwind_tags import *
from dpath.util import get as dget, set as dset
import json
import traceback
# def trackfunccall(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#          = func(*args, **kwargs)

#         return hcgen

#     return hcgenwrapper


def JsonEditor_(key, pcp=[], **kwargs):
    def _f(a, tprefix):
        editor_cbox = jp.Div(
            a=a, classes=tstr(bg/green/100, ppos.relative, *pcp), id="testing")
        _d = JsonEditor(key, tprefix, a=editor_cbox,
                        style='background-color: white; border: 1px solid;', **kwargs)
        editor_cbox.ediv = a
        editor_cbox.apk = f'{tprefix}{key}'
        editor_cbox.apkdbmap = Dict()
        _f.jsonEditor = _d
        _d.postinit()
        return editor_cbox
    return _f


class JsonEditor(JustpyBaseComponent):
    vue_type = 'jsoneditor'
    # chart_types = [] #TODO

    def __init__(self, key, tprefix,  **kwargs):
        self.options = Dict()
        self.style = ''
        self.classes = ''
        self.width = "0px"
        self.height = "0px"
        self.clear = False
        self.show = True
        self.event_propagation = True
        self.update_create = False
        kwargs['temp'] = False
        self.key = key
        self.id = key

        self.tprefix = tprefix
        super().__init__(**kwargs)
        self.apk = f'{tprefix}{key}'
        self.apkdbmap = Dict()
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        # self.allowed_events = [] #TODO
        for com in ['a', 'add_to']:
            if com in kwargs.keys():
                kwargs[com].add_component(self)
        #self.jsontext = "i am jsontext"

    def __repr__(self):
        return f'{self.__class__.__name__}(id: {self.id}, vue_type: {self.vue_type}, chart options: {self.options})'

    def __setattr__(self, key, value):
        if key == 'options':
            if isinstance(value, str):
                self.load_json(value)
            else:
                self.__dict__[key] = value
        else:
            self.__dict__[key] = value

    def set_cfgattr(self, attrpath, attrval):
        dset(self.options, attrpath, attrval)
        self.update_create = True

    def add_to_page(self, wp: WebPage):
        wp.add_component(self)

    def replace_content(self, jsontext):
        self.jsontext = jsontext
        self.update_create = True
        pass

    def add_to(self, *args):
        for c in args:
            c.add_component(self)

    def react(self, data):
        pass

    def load_json(self, options_string):
        self.options = Dict(demjson.decode(
            options_string.encode("ascii", "ignore")))

        return self.options

    def load_json_from_file(self, file_name):
        with open(file_name, 'r') as f:
            self.options = Dict(demjson.decode(
                f.read().encode("ascii", "ignore")))
        return self.options

    def postinit(self):
        pass

    def convert_object_to_dict(self):

        d = {}
        d['vue_type'] = self.vue_type
        d['id'] = self.id
        d['show'] = self.show
        d['classes'] = self.classes
        d['style'] = self.style
        d['event_propagation'] = self.event_propagation
        d['def'] = self.options
        d['jsontext'] = self.jsontext
        #print("jsonEditor:convert_object_to_dict = ", self.jsontext)

        d['events'] = self.events
        d['width'] = self.width
        d['height'] = self.height
        d['clear'] = self.clear
        d['options'] = self.options
        d['update_create'] = self.update_create

        self.update_create = False

        return d
