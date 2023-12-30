module meow(
    output reg l1, l2, l3, l4, l5, l6, l7, l8,
	 input [3:0] col,
	 
	 input clk
);
reg [1:0]state=2'b00;
reg [1:0]nextState=2'b00;

reg [3:0] row;
reg [7:0] keyCode;

// Instantiate the keyboard scanner module
//keyboardScanner scanner_inst (
//    .clk(clk),
//    .col(col),
//    .row(row),
//    .keyCode(keyCode)
//);
always@(posedge clk) begin
    state <= nextState;
end

//output CL
always@(posedge clk) begin
    case (state)
    2'b00: row <= 4'b0001;
    2'b01: row <= 4'b0010;
    2'b10: row <= 4'b0100;
    2'b11: row <= 4'b1000;
    default: row <= 4'b0001;
  endcase
    if (col != 4'b0000) begin
		
		keyCode <= {row[0],row[1],row[2],row[3], col[0],col[1],col[2],col[3]};
		$display ( "time-%0t %Øh%0h%Øh%0h%Øh%0h%Øh%0h%Øh%0h",$time, keyCode[0],keyCode[1],keyCode[2],keyCode[3],keyCode[4],keyCode[5],keyCode[6],keyCode[7]);
    end
end

//next state CL
always @(posedge clk) begin
        case (state)
            2'b00: nextState <= 2'b01;
            2'b01: nextState <= 2'b10;
            2'b10: nextState <= 2'b11;
            2'b11: nextState <= 2'b00;
            default: nextState <= 2'b00;
        endcase
end
// Your logic here - modify as needed
always @(posedge clk) begin
	 
    // Add your logic to control the l1, l2, ..., l8 outputs based on the keyCode or other conditions
    l1 = keyCode[0];
    l2 = keyCode[1];
	 l3 = keyCode[2];
	 l4 = keyCode[3];
	 l5 = keyCode[4];
	 l6 = keyCode[5];
	 l7 = keyCode[6];
	 l8 = keyCode[7];
end

// Provide clock signal and column input for testing
integer i;
initial begin
    // clk = 0;
    //col = 4'b0001;
	 //for (i = 0; i > 5000; i = i + 1) begin
    //    #5 clk = ~clk;  // Toggle the clock every 5 time units
    //    col = 4'b0010;  // Set a sample column value
    //end
    // Add your testbench code here to toggle the clock and set column values
    // Example:
    // for (int i = 0; i < 10; i = i + 1) begin
    //     #5 clk = ~clk;  // Toggle the clock every 5 time units
    //     col = 4'b0010;  // Set a sample column value
    // end
end

endmodule