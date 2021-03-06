# -*- coding: utf-8 -*-
import random
import simpy

class Processor:
    def __init__(self, env, id, latency):
        self.timeout = env.timeout
        self.processor = simpy.Resource(env)
        self.latency = latency
        self.name = 'proc_{}'.format(id)

    def process_message(self, method, value):
        print(self.name + ': scheduling process of message')
        with self.processor.request() as rec:
            yield rec
            yield self.timeout(self.latency)
            for z in method(value):
                yield z
            # try:
            #     iter_call = iter(call)
            #     for z in iter_call:
            #         yield z
            # except TypeError as err:
            #     print(err)
                #print('handle method is not iterable')
            


