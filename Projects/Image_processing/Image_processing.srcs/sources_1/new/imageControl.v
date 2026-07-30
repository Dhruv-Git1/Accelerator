`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 28.07.2026 16:47:27
// Design Name: 
// Module Name: imageControl
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


module imageControl(
    input wire i_clk,
    input wire i_rst,
    input wire [7:0] i_pixel_data,
    input wire i_pixel_data_valid,  // this is coming from camera, saying that now valid data is coming
    output reg [71:0] o_pixel_data,
    output wire o_pixel_data_valid

    );
    //these are now the internal wires as we know
    reg [8:0] pixel_counter;
    reg [1:0] current_write_line_buffer;
    reg [3:0] line_buff_data_valid;       //WHY 4 BITS?, there is data_valid in linebuffer.v also....?
    reg [3:0] line_buff_read_data;
    reg [1:0] current_read_line_buffer;
    
    
    reg  [11:0] total_pixel_counter;   //why 12 bit, is this for 512 pixels?
    reg rd_line_buffer;
    wire [23:0] lb0_data, lb1_data, lb2_data, lb3_data;
    
    //FSM states
    localparam idle = 1'b0;
    localparam RD_BUFFER = 1'b1;
    reg read_state;
    
    
    
    
    //line buffer instantiation (4)
linebuffer lb0 (
.i_clk(i_clk), .i_rst(i_rst), .i_data(i_pixel_data),
.i_data_valid(line_buff_data_valid[0]),
.o_data(),  
.i_rd_data(line_buff_read_data[0]) // ~ ready signal from slave
    );
    
linebuffer lb1 (
.i_clk(i_clk), .i_rst(i_rst), .i_data(i_pixel_data),
.i_data_valid(line_buff_data_valid[1]),
.o_data(),  
.i_rd_data(line_buff_read_data[1]) // ~ ready signal from slave
    );
    
 linebuffer lb2 (
.i_clk(i_clk), .i_rst(i_rst), .i_data(i_pixel_data),
.i_data_valid(line_buff_data_valid[2]),
.o_data(),  
.i_rd_data(line_buff_read_data[2]) // ~ ready signal from slave
    );
 
linebuffer lb3 (
.i_clk(i_clk), .i_rst(i_rst), .i_data(i_pixel_data),
.i_data_valid(line_buff_data_valid[3]),
.o_data(),  
.i_rd_data(line_buff_read_data[3]) // ~ ready signal from slave
    );
     
    
    //code for the demux
    //count 512 pixels and switch write buffers
    always @(posedge i_clk) begin
        if(i_rst) begin
            pixel_counter <= 9'd0;
            current_write_line_buffer <= 2'd0;
        end
            else if (i_pixel_data_valid) 
                begin
                    pixel_counter <= pixel_counter +1;
                    if(pixel_counter == 9'd511) begin
                        current_write_line_buffer <= current_write_line_buffer +1;
                    end
                end
    
    end
    
    always @(*) begin
        line_buff_data_valid = 4'b0000;      //VERY WIERD COMBINATINAL LOGIC, ALWAYS SET TO 0???
        line_buff_data_valid[current_write_line_buffer] = i_pixel_data_valid;
    end
    
    
    //pixel tracker
    //tracks total buffered pixels to decide when to start reading
    always @(posedge i_clk)begin
        if (i_rst) begin
            total_pixel_counter <= 12'd0;
        end
        else begin
            if(i_pixel_data_valid  && !rd_line_buffer)
                total_pixel_counter <= total_pixel_counter +1;
            else if (!i_pixel_data_valid && rd_line_buffer)
                total_pixel_counter <= total_pixel_counter -1;   //  ???why reducing
        end
    end
    
    //read fsm and read counters
    always @(posedge i_clk) begin
        if(i_rst) begin
            read_state <= IDLE;
            rd_line_buffer <= 1'b0;
            current_read_line_buffer <= 2'd0;
        end else begin
            case (read_state)
                IDLE: begin
                    //wait until at least 3 lines are full
                    if (total_pixel_counter >= 12d'1536) begin
                        read_state <= RD_BUFFER;    //what is this RD BUFFER
                        rd_line_buffer <= 1'b1;
                        
                     end
                  end 
                  RD_BUFFER: begin
                    if(read_conter == 9'd511) begin
                        read_
                    end
                    
                  
                  end
                        
                
                
                
    
    end 
    
    
    
    
    
    
endmodule
