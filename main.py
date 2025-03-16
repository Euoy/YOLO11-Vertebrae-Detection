import angle
import cutter


if __name__ == "__main__":

    model_path = "E:\\YOLO11-Vertebrae-Detection\\best.pt"
    dataset_path = "E:\\bone_dataset"
    predict_save_path = "E:\\YOLO11-Vertebrae-Detection\\results\\predicts"
    crop_save_path = "E:\\YOLO11-Vertebrae-Detection\\results\\crops"
    csv_save_path = "E:\\YOLO11-Vertebrae-Detection\\results"
    fig_save_path = "E:\\YOLO11-Vertebrae-Detection\\results\\figs"

    # cutter = cutter.Cutter(model_path, dataset_path, predict_save_path, crop_save_path, csv_save_path)
    # cutter.run()

    # print("cut and croods save done!")

    angle_calculator = angle.AngleSVACalculator(crop_save_path + "\\c2", crop_save_path + "\\c7", csv_save_path + "\\c2.csv", csv_save_path + "\\c7.csv", dataset_path, fig_save_path)
    angle_calculator.run()

    print("angle done!")