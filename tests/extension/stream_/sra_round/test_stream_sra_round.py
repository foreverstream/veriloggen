from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_sra_round

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
#from pprint import pprint

expected_verilog = """
module test
(

);

  reg CLK;
  reg RST;
  reg signed [32-1:0] xdata;
  reg signed [32-1:0] ydata;
  wire signed [32-1:0] zdata;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .ydata(ydata),
    .zdata(zdata)
  );

  reg reset_done;
  reg end_of_sim;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    reset_done = 0;
    xdata = 0;
    ydata = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #10;
    @(posedge end_of_sim);
    #100;
    $finish;
  end

  reg [32-1:0] send_fsm;
  localparam send_fsm_init = 0;
  reg [32-1:0] send_count;
  reg [32-1:0] recv_fsm;
  localparam recv_fsm_init = 0;
  reg [32-1:0] recv_count;
  localparam send_fsm_1 = 1;
  localparam send_fsm_2 = 2;
  localparam send_fsm_3 = 3;
  localparam send_fsm_4 = 4;
  localparam send_fsm_5 = 5;
  localparam send_fsm_6 = 6;
  localparam send_fsm_7 = 7;
  localparam send_fsm_8 = 8;
  localparam send_fsm_9 = 9;
  localparam send_fsm_10 = 10;
  localparam send_fsm_11 = 11;
  localparam send_fsm_12 = 12;
  localparam send_fsm_13 = 13;
  localparam send_fsm_14 = 14;
  localparam send_fsm_15 = 15;
  localparam send_fsm_16 = 16;
  localparam send_fsm_17 = 17;
  localparam send_fsm_18 = 18;
  localparam send_fsm_19 = 19;
  localparam send_fsm_20 = 20;
  localparam send_fsm_21 = 21;
  localparam send_fsm_22 = 22;
  localparam send_fsm_23 = 23;
  localparam send_fsm_24 = 24;
  localparam send_fsm_25 = 25;
  localparam send_fsm_26 = 26;
  localparam send_fsm_27 = 27;
  localparam send_fsm_28 = 28;
  localparam send_fsm_29 = 29;
  localparam send_fsm_30 = 30;
  localparam send_fsm_31 = 31;
  localparam send_fsm_32 = 32;
  localparam send_fsm_33 = 33;
  localparam send_fsm_34 = 34;
  localparam send_fsm_35 = 35;
  localparam send_fsm_36 = 36;
  localparam send_fsm_37 = 37;
  localparam send_fsm_38 = 38;
  localparam send_fsm_39 = 39;
  localparam send_fsm_40 = 40;
  localparam send_fsm_41 = 41;
  localparam send_fsm_42 = 42;
  localparam send_fsm_43 = 43;
  localparam send_fsm_44 = 44;
  localparam send_fsm_45 = 45;
  localparam send_fsm_46 = 46;
  localparam send_fsm_47 = 47;
  localparam send_fsm_48 = 48;
  localparam send_fsm_49 = 49;
  localparam send_fsm_50 = 50;
  localparam send_fsm_51 = 51;
  localparam send_fsm_52 = 52;
  localparam send_fsm_53 = 53;
  localparam send_fsm_54 = 54;
  localparam send_fsm_55 = 55;
  localparam send_fsm_56 = 56;
  localparam send_fsm_57 = 57;
  localparam send_fsm_58 = 58;
  localparam send_fsm_59 = 59;
  localparam send_fsm_60 = 60;
  localparam send_fsm_61 = 61;
  localparam send_fsm_62 = 62;
  localparam send_fsm_63 = 63;
  localparam send_fsm_64 = 64;
  localparam send_fsm_65 = 65;
  localparam send_fsm_66 = 66;
  localparam send_fsm_67 = 67;
  localparam send_fsm_68 = 68;
  localparam send_fsm_69 = 69;
  localparam send_fsm_70 = 70;
  localparam send_fsm_71 = 71;
  localparam send_fsm_72 = 72;
  localparam send_fsm_73 = 73;
  localparam send_fsm_74 = 74;
  localparam send_fsm_75 = 75;
  localparam send_fsm_76 = 76;
  localparam send_fsm_77 = 77;
  localparam send_fsm_78 = 78;
  localparam send_fsm_79 = 79;
  localparam send_fsm_80 = 80;
  localparam send_fsm_81 = 81;

  always @(posedge CLK) begin
    if(RST) begin
      send_fsm <= send_fsm_init;
      send_count <= 0;
    end else begin
      case(send_fsm)
        send_fsm_init: begin
          if(reset_done) begin
            send_fsm <= send_fsm_1;
          end 
        end
        send_fsm_1: begin
          xdata <= -2147483648;
          ydata <= 0;
          send_count <= 0;
          send_fsm <= send_fsm_2;
        end
        send_fsm_2: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_3;
          end 
        end
        send_fsm_3: begin
          xdata <= -10;
          ydata <= 0;
          send_count <= 0;
          send_fsm <= send_fsm_4;
        end
        send_fsm_4: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_5;
          end 
        end
        send_fsm_5: begin
          xdata <= 1;
          ydata <= 0;
          send_count <= 0;
          send_fsm <= send_fsm_6;
        end
        send_fsm_6: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_7;
          end 
        end
        send_fsm_7: begin
          xdata <= 2147483637;
          ydata <= 0;
          send_count <= 0;
          send_fsm <= send_fsm_8;
        end
        send_fsm_8: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_9;
          end 
        end
        send_fsm_9: begin
          xdata <= -2147483648;
          ydata <= 1;
          send_count <= 0;
          send_fsm <= send_fsm_10;
        end
        send_fsm_10: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_11;
          end 
        end
        send_fsm_11: begin
          xdata <= -10;
          ydata <= 1;
          send_count <= 0;
          send_fsm <= send_fsm_12;
        end
        send_fsm_12: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_13;
          end 
        end
        send_fsm_13: begin
          xdata <= 1;
          ydata <= 1;
          send_count <= 0;
          send_fsm <= send_fsm_14;
        end
        send_fsm_14: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_15;
          end 
        end
        send_fsm_15: begin
          xdata <= 2147483637;
          ydata <= 1;
          send_count <= 0;
          send_fsm <= send_fsm_16;
        end
        send_fsm_16: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_17;
          end 
        end
        send_fsm_17: begin
          xdata <= -2147483648;
          ydata <= 2;
          send_count <= 0;
          send_fsm <= send_fsm_18;
        end
        send_fsm_18: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_19;
          end 
        end
        send_fsm_19: begin
          xdata <= -10;
          ydata <= 2;
          send_count <= 0;
          send_fsm <= send_fsm_20;
        end
        send_fsm_20: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_21;
          end 
        end
        send_fsm_21: begin
          xdata <= 1;
          ydata <= 2;
          send_count <= 0;
          send_fsm <= send_fsm_22;
        end
        send_fsm_22: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_23;
          end 
        end
        send_fsm_23: begin
          xdata <= 2147483637;
          ydata <= 2;
          send_count <= 0;
          send_fsm <= send_fsm_24;
        end
        send_fsm_24: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_25;
          end 
        end
        send_fsm_25: begin
          xdata <= -2147483648;
          ydata <= 3;
          send_count <= 0;
          send_fsm <= send_fsm_26;
        end
        send_fsm_26: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_27;
          end 
        end
        send_fsm_27: begin
          xdata <= -10;
          ydata <= 3;
          send_count <= 0;
          send_fsm <= send_fsm_28;
        end
        send_fsm_28: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_29;
          end 
        end
        send_fsm_29: begin
          xdata <= 1;
          ydata <= 3;
          send_count <= 0;
          send_fsm <= send_fsm_30;
        end
        send_fsm_30: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_31;
          end 
        end
        send_fsm_31: begin
          xdata <= 2147483637;
          ydata <= 3;
          send_count <= 0;
          send_fsm <= send_fsm_32;
        end
        send_fsm_32: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_33;
          end 
        end
        send_fsm_33: begin
          xdata <= -2147483648;
          ydata <= 15;
          send_count <= 0;
          send_fsm <= send_fsm_34;
        end
        send_fsm_34: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_35;
          end 
        end
        send_fsm_35: begin
          xdata <= -10;
          ydata <= 15;
          send_count <= 0;
          send_fsm <= send_fsm_36;
        end
        send_fsm_36: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_37;
          end 
        end
        send_fsm_37: begin
          xdata <= 1;
          ydata <= 15;
          send_count <= 0;
          send_fsm <= send_fsm_38;
        end
        send_fsm_38: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_39;
          end 
        end
        send_fsm_39: begin
          xdata <= 2147483637;
          ydata <= 15;
          send_count <= 0;
          send_fsm <= send_fsm_40;
        end
        send_fsm_40: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_41;
          end 
        end
        send_fsm_41: begin
          xdata <= -2147483648;
          ydata <= 16;
          send_count <= 0;
          send_fsm <= send_fsm_42;
        end
        send_fsm_42: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_43;
          end 
        end
        send_fsm_43: begin
          xdata <= -10;
          ydata <= 16;
          send_count <= 0;
          send_fsm <= send_fsm_44;
        end
        send_fsm_44: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_45;
          end 
        end
        send_fsm_45: begin
          xdata <= 1;
          ydata <= 16;
          send_count <= 0;
          send_fsm <= send_fsm_46;
        end
        send_fsm_46: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_47;
          end 
        end
        send_fsm_47: begin
          xdata <= 2147483637;
          ydata <= 16;
          send_count <= 0;
          send_fsm <= send_fsm_48;
        end
        send_fsm_48: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_49;
          end 
        end
        send_fsm_49: begin
          xdata <= -2147483648;
          ydata <= 17;
          send_count <= 0;
          send_fsm <= send_fsm_50;
        end
        send_fsm_50: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_51;
          end 
        end
        send_fsm_51: begin
          xdata <= -10;
          ydata <= 17;
          send_count <= 0;
          send_fsm <= send_fsm_52;
        end
        send_fsm_52: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_53;
          end 
        end
        send_fsm_53: begin
          xdata <= 1;
          ydata <= 17;
          send_count <= 0;
          send_fsm <= send_fsm_54;
        end
        send_fsm_54: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_55;
          end 
        end
        send_fsm_55: begin
          xdata <= 2147483637;
          ydata <= 17;
          send_count <= 0;
          send_fsm <= send_fsm_56;
        end
        send_fsm_56: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_57;
          end 
        end
        send_fsm_57: begin
          xdata <= -2147483648;
          ydata <= 30;
          send_count <= 0;
          send_fsm <= send_fsm_58;
        end
        send_fsm_58: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_59;
          end 
        end
        send_fsm_59: begin
          xdata <= -10;
          ydata <= 30;
          send_count <= 0;
          send_fsm <= send_fsm_60;
        end
        send_fsm_60: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_61;
          end 
        end
        send_fsm_61: begin
          xdata <= 1;
          ydata <= 30;
          send_count <= 0;
          send_fsm <= send_fsm_62;
        end
        send_fsm_62: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_63;
          end 
        end
        send_fsm_63: begin
          xdata <= 2147483637;
          ydata <= 30;
          send_count <= 0;
          send_fsm <= send_fsm_64;
        end
        send_fsm_64: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_65;
          end 
        end
        send_fsm_65: begin
          xdata <= -2147483648;
          ydata <= 31;
          send_count <= 0;
          send_fsm <= send_fsm_66;
        end
        send_fsm_66: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_67;
          end 
        end
        send_fsm_67: begin
          xdata <= -10;
          ydata <= 31;
          send_count <= 0;
          send_fsm <= send_fsm_68;
        end
        send_fsm_68: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_69;
          end 
        end
        send_fsm_69: begin
          xdata <= 1;
          ydata <= 31;
          send_count <= 0;
          send_fsm <= send_fsm_70;
        end
        send_fsm_70: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_71;
          end 
        end
        send_fsm_71: begin
          xdata <= 2147483637;
          ydata <= 31;
          send_count <= 0;
          send_fsm <= send_fsm_72;
        end
        send_fsm_72: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_73;
          end 
        end
        send_fsm_73: begin
          xdata <= -2147483648;
          ydata <= 32;
          send_count <= 0;
          send_fsm <= send_fsm_74;
        end
        send_fsm_74: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_75;
          end 
        end
        send_fsm_75: begin
          xdata <= -10;
          ydata <= 32;
          send_count <= 0;
          send_fsm <= send_fsm_76;
        end
        send_fsm_76: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_77;
          end 
        end
        send_fsm_77: begin
          xdata <= 1;
          ydata <= 32;
          send_count <= 0;
          send_fsm <= send_fsm_78;
        end
        send_fsm_78: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_79;
          end 
        end
        send_fsm_79: begin
          xdata <= 2147483637;
          ydata <= 32;
          send_count <= 0;
          send_fsm <= send_fsm_80;
        end
        send_fsm_80: begin
          xdata <= xdata + 1;
          send_count <= send_count + 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          if(send_count == 9) begin
            send_fsm <= send_fsm_81;
          end 
        end
      endcase
    end
  end

  localparam recv_fsm_1 = 1;
  localparam recv_fsm_2 = 2;
  localparam recv_fsm_3 = 3;
  localparam recv_fsm_4 = 4;
  localparam recv_fsm_5 = 5;
  localparam recv_fsm_6 = 6;
  localparam recv_fsm_7 = 7;
  localparam recv_fsm_8 = 8;
  localparam recv_fsm_9 = 9;
  localparam recv_fsm_10 = 10;
  localparam recv_fsm_11 = 11;
  localparam recv_fsm_12 = 12;
  localparam recv_fsm_13 = 13;
  localparam recv_fsm_14 = 14;
  localparam recv_fsm_15 = 15;
  localparam recv_fsm_16 = 16;
  localparam recv_fsm_17 = 17;
  localparam recv_fsm_18 = 18;
  localparam recv_fsm_19 = 19;
  localparam recv_fsm_20 = 20;
  localparam recv_fsm_21 = 21;
  localparam recv_fsm_22 = 22;
  localparam recv_fsm_23 = 23;
  localparam recv_fsm_24 = 24;
  localparam recv_fsm_25 = 25;
  localparam recv_fsm_26 = 26;
  localparam recv_fsm_27 = 27;
  localparam recv_fsm_28 = 28;
  localparam recv_fsm_29 = 29;
  localparam recv_fsm_30 = 30;
  localparam recv_fsm_31 = 31;
  localparam recv_fsm_32 = 32;
  localparam recv_fsm_33 = 33;
  localparam recv_fsm_34 = 34;
  localparam recv_fsm_35 = 35;
  localparam recv_fsm_36 = 36;
  localparam recv_fsm_37 = 37;
  localparam recv_fsm_38 = 38;
  localparam recv_fsm_39 = 39;
  localparam recv_fsm_40 = 40;
  localparam recv_fsm_41 = 41;
  localparam recv_fsm_42 = 42;
  localparam recv_fsm_43 = 43;
  localparam recv_fsm_44 = 44;
  localparam recv_fsm_45 = 45;
  localparam recv_fsm_46 = 46;
  localparam recv_fsm_47 = 47;
  localparam recv_fsm_48 = 48;
  localparam recv_fsm_49 = 49;
  localparam recv_fsm_50 = 50;
  localparam recv_fsm_51 = 51;
  localparam recv_fsm_52 = 52;
  localparam recv_fsm_53 = 53;
  localparam recv_fsm_54 = 54;
  localparam recv_fsm_55 = 55;
  localparam recv_fsm_56 = 56;
  localparam recv_fsm_57 = 57;
  localparam recv_fsm_58 = 58;
  localparam recv_fsm_59 = 59;
  localparam recv_fsm_60 = 60;
  localparam recv_fsm_61 = 61;
  localparam recv_fsm_62 = 62;
  localparam recv_fsm_63 = 63;
  localparam recv_fsm_64 = 64;
  localparam recv_fsm_65 = 65;
  localparam recv_fsm_66 = 66;
  localparam recv_fsm_67 = 67;
  localparam recv_fsm_68 = 68;
  localparam recv_fsm_69 = 69;
  localparam recv_fsm_70 = 70;
  localparam recv_fsm_71 = 71;
  localparam recv_fsm_72 = 72;
  localparam recv_fsm_73 = 73;
  localparam recv_fsm_74 = 74;
  localparam recv_fsm_75 = 75;
  localparam recv_fsm_76 = 76;
  localparam recv_fsm_77 = 77;
  localparam recv_fsm_78 = 78;
  localparam recv_fsm_79 = 79;
  localparam recv_fsm_80 = 80;
  localparam recv_fsm_81 = 81;
  localparam recv_fsm_82 = 82;
  localparam recv_fsm_83 = 83;

  always @(posedge CLK) begin
    if(RST) begin
      recv_fsm <= recv_fsm_init;
      recv_count <= 0;
      end_of_sim <= 0;
    end else begin
      case(recv_fsm)
        recv_fsm_init: begin
          if(reset_done) begin
            recv_fsm <= recv_fsm_1;
          end 
        end
        recv_fsm_1: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_2;
        end
        recv_fsm_2: begin
          if(recv_count < 5) begin
            recv_count <= recv_count + 1;
          end else begin
            recv_count <= 0;
          end
          if(recv_count >= 5) begin
            recv_fsm <= recv_fsm_3;
          end 
        end
        recv_fsm_3: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_4;
        end
        recv_fsm_4: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_5;
          end 
        end
        recv_fsm_5: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_6;
        end
        recv_fsm_6: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_7;
          end 
        end
        recv_fsm_7: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_8;
        end
        recv_fsm_8: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_9;
          end 
        end
        recv_fsm_9: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_10;
        end
        recv_fsm_10: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_11;
          end 
        end
        recv_fsm_11: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_12;
        end
        recv_fsm_12: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_13;
          end 
        end
        recv_fsm_13: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_14;
        end
        recv_fsm_14: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_15;
          end 
        end
        recv_fsm_15: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_16;
        end
        recv_fsm_16: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_17;
          end 
        end
        recv_fsm_17: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_18;
        end
        recv_fsm_18: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_19;
          end 
        end
        recv_fsm_19: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_20;
        end
        recv_fsm_20: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_21;
          end 
        end
        recv_fsm_21: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_22;
        end
        recv_fsm_22: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_23;
          end 
        end
        recv_fsm_23: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_24;
        end
        recv_fsm_24: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_25;
          end 
        end
        recv_fsm_25: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_26;
        end
        recv_fsm_26: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_27;
          end 
        end
        recv_fsm_27: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_28;
        end
        recv_fsm_28: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_29;
          end 
        end
        recv_fsm_29: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_30;
        end
        recv_fsm_30: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_31;
          end 
        end
        recv_fsm_31: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_32;
        end
        recv_fsm_32: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_33;
          end 
        end
        recv_fsm_33: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_34;
        end
        recv_fsm_34: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_35;
          end 
        end
        recv_fsm_35: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_36;
        end
        recv_fsm_36: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_37;
          end 
        end
        recv_fsm_37: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_38;
        end
        recv_fsm_38: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_39;
          end 
        end
        recv_fsm_39: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_40;
        end
        recv_fsm_40: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_41;
          end 
        end
        recv_fsm_41: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_42;
        end
        recv_fsm_42: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_43;
          end 
        end
        recv_fsm_43: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_44;
        end
        recv_fsm_44: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_45;
          end 
        end
        recv_fsm_45: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_46;
        end
        recv_fsm_46: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_47;
          end 
        end
        recv_fsm_47: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_48;
        end
        recv_fsm_48: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_49;
          end 
        end
        recv_fsm_49: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_50;
        end
        recv_fsm_50: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_51;
          end 
        end
        recv_fsm_51: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_52;
        end
        recv_fsm_52: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_53;
          end 
        end
        recv_fsm_53: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_54;
        end
        recv_fsm_54: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_55;
          end 
        end
        recv_fsm_55: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_56;
        end
        recv_fsm_56: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_57;
          end 
        end
        recv_fsm_57: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_58;
        end
        recv_fsm_58: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_59;
          end 
        end
        recv_fsm_59: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_60;
        end
        recv_fsm_60: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_61;
          end 
        end
        recv_fsm_61: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_62;
        end
        recv_fsm_62: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_63;
          end 
        end
        recv_fsm_63: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_64;
        end
        recv_fsm_64: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_65;
          end 
        end
        recv_fsm_65: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_66;
        end
        recv_fsm_66: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_67;
          end 
        end
        recv_fsm_67: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_68;
        end
        recv_fsm_68: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_69;
          end 
        end
        recv_fsm_69: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_70;
        end
        recv_fsm_70: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_71;
          end 
        end
        recv_fsm_71: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_72;
        end
        recv_fsm_72: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_73;
          end 
        end
        recv_fsm_73: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_74;
        end
        recv_fsm_74: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_75;
          end 
        end
        recv_fsm_75: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_76;
        end
        recv_fsm_76: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_77;
          end 
        end
        recv_fsm_77: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_78;
        end
        recv_fsm_78: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_79;
          end 
        end
        recv_fsm_79: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_80;
        end
        recv_fsm_80: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_81;
          end 
        end
        recv_fsm_81: begin
          recv_count <= 0;
          recv_fsm <= recv_fsm_82;
        end
        recv_fsm_82: begin
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 9) begin
            recv_fsm <= recv_fsm_83;
          end 
        end
        recv_fsm_83: begin
          end_of_sim <= 1;
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  input signed [32-1:0] xdata,
  input signed [32-1:0] ydata,
  output signed [32-1:0] zdata
);

  reg [1-1:0] _pointer_data_2;
  reg [5-1:0] _slice_data_8;
  reg [1-1:0] _eq_data_24;
  reg signed [32-1:0] __delay_data_26;
  reg signed [32-1:0] __delay_data_31;
  reg [5-1:0] _minus_data_9;
  reg signed [2-1:0] _cond_data_19;
  reg signed [32-1:0] __delay_data_27;
  reg signed [32-1:0] __delay_data_32;
  reg [1-1:0] __delay_data_36;
  reg signed [34-1:0] _sll_data_11;
  reg signed [32-1:0] __delay_data_28;
  reg signed [2-1:0] __delay_data_29;
  reg signed [32-1:0] __delay_data_33;
  reg [1-1:0] __delay_data_37;
  reg signed [34-1:0] _plus_data_20;
  reg signed [2-1:0] __delay_data_30;
  reg signed [32-1:0] __delay_data_34;
  reg [1-1:0] __delay_data_38;
  reg signed [32-1:0] __delay_data_41;
  reg signed [34-1:0] _plus_data_21;
  reg signed [32-1:0] __delay_data_35;
  reg [1-1:0] __delay_data_39;
  reg signed [32-1:0] __delay_data_42;
  reg signed [32-1:0] _sra_data_22;
  reg [1-1:0] __delay_data_40;
  reg signed [32-1:0] __delay_data_43;
  reg signed [32-1:0] _cond_data_25;
  assign zdata = _cond_data_25;

  always @(posedge CLK) begin
    if(RST) begin
      _pointer_data_2 <= 0;
      _slice_data_8 <= 0;
      _eq_data_24 <= 0;
      __delay_data_26 <= 0;
      __delay_data_31 <= 0;
      _minus_data_9 <= 0;
      _cond_data_19 <= 0;
      __delay_data_27 <= 0;
      __delay_data_32 <= 0;
      __delay_data_36 <= 0;
      _sll_data_11 <= 0;
      __delay_data_28 <= 0;
      __delay_data_29 <= 0;
      __delay_data_33 <= 0;
      __delay_data_37 <= 0;
      _plus_data_20 <= 0;
      __delay_data_30 <= 0;
      __delay_data_34 <= 0;
      __delay_data_38 <= 0;
      __delay_data_41 <= 0;
      _plus_data_21 <= 0;
      __delay_data_35 <= 0;
      __delay_data_39 <= 0;
      __delay_data_42 <= 0;
      _sra_data_22 <= 0;
      __delay_data_40 <= 0;
      __delay_data_43 <= 0;
      _cond_data_25 <= 0;
    end else begin
      _pointer_data_2 <= xdata[6'sd31];
      _slice_data_8 <= ydata[4'd4:1'd0];
      _eq_data_24 <= ydata == 1'sd0;
      __delay_data_26 <= xdata;
      __delay_data_31 <= ydata;
      _minus_data_9 <= _slice_data_8 - 2'sd1;
      _cond_data_19 <= (_pointer_data_2)? -2'sd1 : 1'sd0;
      __delay_data_27 <= __delay_data_26;
      __delay_data_32 <= __delay_data_31;
      __delay_data_36 <= _eq_data_24;
      _sll_data_11 <= 2'sd1 << _minus_data_9;
      __delay_data_28 <= __delay_data_27;
      __delay_data_29 <= _cond_data_19;
      __delay_data_33 <= __delay_data_32;
      __delay_data_37 <= __delay_data_36;
      _plus_data_20 <= __delay_data_28 + _sll_data_11;
      __delay_data_30 <= __delay_data_29;
      __delay_data_34 <= __delay_data_33;
      __delay_data_38 <= __delay_data_37;
      __delay_data_41 <= __delay_data_28;
      _plus_data_21 <= _plus_data_20 + __delay_data_30;
      __delay_data_35 <= __delay_data_34;
      __delay_data_39 <= __delay_data_38;
      __delay_data_42 <= __delay_data_41;
      _sra_data_22 <= _plus_data_21 >>> __delay_data_35;
      __delay_data_40 <= __delay_data_39;
      __delay_data_43 <= __delay_data_42;
      _cond_data_25 <= (__delay_data_40)? __delay_data_43 : _sra_data_22;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_sra_round.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)

    # run simulator (Icarus Verilog)
    sim = veriloggen.simulation.Simulator(test_module)
    rslt = sim.run()  # display=False
    #rslt = sim.run(display=True)
    print(rslt)

    vx = list(map(lambda x: int(str.split(x,"=")[1]), filter(lambda x: "xdata" in x  , str.split(rslt, "\n"))))
    vy = list(map(lambda x: int(str.split(x,"=")[1]), filter(lambda x: "ydata" in x  , str.split(rslt, "\n"))))
    vz = list(map(lambda x: int(str.split(x,"=")[1]), filter(lambda x: "zdata" in x  , str.split(rslt, "\n"))))
    ez = list(map(lambda x,y: int( Decimal(str(x/(2.0**y))).quantize(Decimal('0'), rounding=ROUND_HALF_UP)), vx,vy))

    #pprint(list(zip(lx,ly,lz,ez)))

    assert(all(map(lambda x ,y: x == y, vz,ez)))

