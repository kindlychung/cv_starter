#include <QCoreApplication>
#include <iostream>
#include <opencv2/opencv.hpp>
int main(int argc, char** argv) {
    using namespace cv;
    QCoreApplication app(argc, argv);
    Mat image = imread(argv[1]);
    imshow("Image", image);
    return app.exec();
}
