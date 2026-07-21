# 0 "D:\\Desktop\\Accelerator\\chal_ja_bhai\\platform\\zynq_fsbl\\zynq_fsbl_bsp\\lop-config.dts"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "D:\\Desktop\\Accelerator\\chal_ja_bhai\\platform\\zynq_fsbl\\zynq_fsbl_bsp\\lop-config.dts"

/dts-v1/;
/ {
        compatible = "system-device-tree-v1,lop";
        lops {
                lop_0 {
                        compatible = "system-device-tree-v1,lop,load";
                        load = "assists/baremetal_validate_comp_xlnx.py";
                };

                lop_1 {
                    compatible = "system-device-tree-v1,lop,assist-v1";
                    node = "/";
                    outdir = "D:/Desktop/Accelerator/chal_ja_bhai/platform/zynq_fsbl/zynq_fsbl_bsp";
                    id = "module,baremetal_validate_comp_xlnx";
                    options = "ps7_cortexa9_0 C:/vivado_2024/Vitis/2024.2/data/embeddedsw/lib/sw_services/xilffs_v5_3/src C:/Users/nisha/AppData/Local/Temp/rigel_lopper_nisha8401837615694900249/.repo.yaml";
                };

                lop_2 {
                    compatible = "system-device-tree-v1,lop,assist-v1";
                    node = "/";
                    outdir = "D:/Desktop/Accelerator/chal_ja_bhai/platform/zynq_fsbl/zynq_fsbl_bsp";
                    id = "module,baremetal_validate_comp_xlnx";
                    options = "ps7_cortexa9_0 C:/vivado_2024/Vitis/2024.2/data/embeddedsw/lib/sw_services/xilrsa_v1_8/src C:/Users/nisha/AppData/Local/Temp/rigel_lopper_nisha8401837615694900249/.repo.yaml";
                };

        };
    };
