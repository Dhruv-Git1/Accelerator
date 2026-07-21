//whatever data we are writing to the ip, we want to sent to the led, this is our mission.
#include "xparameters.h"
#include "xil_io.h"

int main() {
    // Write 0xFF (all 8 LEDs ON) to the AXI GPIO base address
    Xil_Out32(XPAR_AXI_GPIO_0_BASEADDR, 0xFF);
    
    return 0;
}

// Xil_out8()