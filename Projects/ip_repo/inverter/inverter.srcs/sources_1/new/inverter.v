`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 25.07.2026 16:37:18
// Design Name: 
// Module Name: inverter
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module inverter
  #(parameter DATA_WIDTH=32)(                    //we have made this parameter so that we can change this later
    input axi_clk,
    input axi_reset_n,  //active low reset in axi
//axi4 s slave to recieving data
//we'll use the style of xilinx
input s_axis_valid,
input [DATA_WIDTH-1 :0] s_axis_data,
output s_axis_ready,
//axi4 s master to send data
output reg m_axis_valid,
output reg [DATA_WIDTH-1:0] m_axis_data,   
input m_axis_ready
    );
    //take this data byte by byte, subtract 255, and give it to m_axis_data
    integer i;
    
    //if our slave not ablt to accept data then we are not ready
    assign s_axis_ready = m_axis_ready;
    always@(posedge axi_clk)
    begin
    //valid data + we are ready to accept it
          if (s_axis_valid & s_axis_ready)
             begin
//                m_axis_data[7:0] <= 255-m_axis_data[7:0];
//                m_axis_data[15:8] <= 255-m_axis_data[15:8];
//                m_axis_data[23:16] <= 255-m_axis_data[23:16];
//                m_axis_data[31:24] <= 255-m_axis_data[31:24];
                  for(i=0; i<DATA_WIDTH/8; i=i+1)
                    begin
              //      m_axis_data[i*8+7 :i*8]  ---> we can't do this, there can't be variable in both sides
                    m_axis_data[i*8 +:8] <= 255- s_axis_data[i*8 + :8];
                    end
             end
    
    end
    
    always @(posedge axi_clk)
    begin 
        m_axis_valid <= s_axis_valid & s_axis_ready; 
    end
    
    
endmodule
