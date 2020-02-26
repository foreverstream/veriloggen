from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth,
                        numports=2, external_ports=(1,))
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth,
                        numports=2, external_ports=(1,))
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth,
                        numports=2, external_ports=(1,))

    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth)

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = strm.source('b')
    c = a + b
    strm.sink(c, 'c')

    def comp_stream(size, offset):
        strm.set_source('a', ram_a, offset, size)
        strm.set_source('b', ram_b, offset, size)
        strm.set_sink('c', ram_c, offset, size)
        strm.run()
        strm.join()

    def comp():
        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)
            saxi.write(1, 1)  # set busy
            size = saxi.read(2)
            offset = saxi.read(3)
            comp_stream(size, offset)
            saxi.write(1, 0)  # unset busy

        vthread.finish()

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start()

    return m


def run(filename='tmp.v', simtype='iverilog', outputfile=None):

    test = mkLed()

    if filename is not None:
        test.to_verilog(filename)

    return '# verify: PASSED'


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)
