#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

class CSV_operation:
    def __init__(self,filename):
        self.filename=filename

    def close_file_write(self):
        self.csvfile_write.close()

    def close_file_read(self):
        self.csvfile_read.close()

    def open_for_write(self):
        self.csvfile_write = open(self.filename, 'wb')
        self.writer = csv.writer(self.csvfile_write)

    def open_for_addData(self):
        self.csvfile_write = open(self.filename, 'a+')
        self.writer = csv.writer(self.csvfile_write)

    def write_csv(self,data):
        self.writer.writerow(data)

    def open_for_read(self):
        self.csvfile_read = open(self.filename,'rb')
        self.reader = csv.reader(self.csvfile_read)

    def read_csv(self):
        for line in self.reader:
            print line

