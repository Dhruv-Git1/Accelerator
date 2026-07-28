`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 28.07.2026 12:32:21
// Design Name: 
// Module Name: conv
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


module conv(
input wire i_clk,
input wire [71:0] i_pixel_data,
input wire  i_pixel_data_valid,
output reg [7:0] o_convolved_data,
output reg o_convolved_data_valid
    );
    
    integer i;
    
    reg kernel [8:0];
    
    initial
         begin
            for (i=0; i<9; i=i+1) begin
            kernel [i] = 1'b1;  // we are initialising the kernel
            
            end
    end
    
    reg [15:0] mult_data [8:0];
    reg mult_data_valid;
    
    always@(posedge i_clk) begin
        for (i=0; i<9; i=i+1)
        begin
            mult_data[i] <= i_pixel_data[i*8 +:8] * kernel[i];
        end
        mult_data_valid <= i_pixel_data_valid;
    end
    
    //pipeline 2 accumulation
    
    reg [15:0] sum_data_int;
    reg [15:0] sum_data;
    reg sum_data_valid;
    
    integer j;
    always@(*) begin
        sum_data_int= 16'b0;
            for (j=0; j<9; j=j+1) begin
            sum_data_int = sum_data_int+ mult_data[j];
        end
    end
    //registering the imtermediate sum
    always @(posedge i_clk) begin
          sum_data  <= sum_data_int;
          sum_data_valid <= mult_data_valid;
    end
    
    //pipeline 3, division
    always @(posedge i_clk) begin
            o_convolved_data <= sum_data/9;
            o_convolved_data_valid <= sum_data_valid;
    end 
    
    
    
    
    
endmodule
