import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        QApplication.setStyle(QStyleFactory.create('Fusion'))


        dynamicViscosityLabel = QLabel("流体粘度：")
        self.dynamicViscosityComboBox = QComboBox()
        self.dynamicViscosityComboBox.addItem("Water：1.01E-3 Pa·s")
        self.dynamicViscosityComboBox.addItems(["Air：17.9E-6 Pa·s"])

        densityLabel = QLabel("流体密度：")
        self.densityComboBox = QComboBox()
        self.densityComboBox.addItem("Water：998 kg/m^3")
        self.densityComboBox.addItems(["Air：1.293 kg/m^3"])

        velocityLable = QLabel("来流速度：")
        self.velocitySpinBox = QDoubleSpinBox()
        self.velocitySpinBox.setDecimals(4)
        self.velocitySpinBox.setRange(0, 300000000)
        self.velocitySpinBox.setValue(1)
        self.velocitySpinBox.setSuffix(" m/s")

        lengthLable = QLabel("特征长度：")
        self.lengthSpinBox = QDoubleSpinBox()
        self.lengthSpinBox.setDecimals(4)        
        self.lengthSpinBox.setRange(0, 999999999)
        self.lengthSpinBox.setValue(7)
        self.lengthSpinBox.setSuffix(" m")

        yPlusLable = QLabel("y+值：")
        yPlusLable.setToolTip("壁面函数要求 30 < y+ < 300\n大涡模拟LES要求 y+ < 1") 
        self.yPlusSpinBox = QDoubleSpinBox()
        self.yPlusSpinBox.setRange(0, 999999999)
        self.yPlusSpinBox.setValue(30)

        ReLabel = QLabel("雷诺数：")
        self.ReLabel = QLabel()

        CfLabel = QLabel("摩擦系数：")
        self.CfLabel = QLabel()

        tauLabel = QLabel("剪切应力：")
        self.tauLabel = QLabel()

        U_tauLabel = QLabel("估算速度：")
        self.U_tauLabel = QLabel()       

        yLabel = QLabel("首层高度：")
        yLabel.setStyleSheet("color:red")
        self.yLabel = QLabel()

        turbuIntensityLabel = QLabel("湍流强度：")
        turbuIntensityLabel.setToolTip("Turbulence Intensity\nI <  1%, 低强度\nI > 10%, 高强度\nI =  5%，中等强度") 
        self.turbuIntensityLabel = QLabel()

        turbuLengthLabel = QLabel("湍流尺度：")
        turbuLengthLabel.setToolTip("Turbulence Length Scale")
        self.turbuLengthLabel = QLabel()

        turbuKineticEnergyLabel = QLabel("湍动能：")
        turbuKineticEnergyLabel.setToolTip("Turbulence Kinetic Energy")
        self.turbuKineticEnergyLabel = QLabel()

        turbuDissipationLabel = QLabel("湍流耗散率：")
        turbuDissipationLabel.setToolTip("Turbulence Dissipation Rate")
        self.turbuDissipationLabel = QLabel()

        omegaLabel = QLabel("Omega：")
        omegaLabel.setToolTip("Specific Dissipation Rate")
        self.omegaLabel = QLabel()

        turbuViscosityRatioLabel = QLabel("湍流粘度比：")
        turbuViscosityRatioLabel.setToolTip("Turbulent Viscosity Ratio")
        turbuViscosityRatioLabel2 = QLabel("1 ~ 10 之间")
        turbuViscosityRatioLabel2.setToolTip("对于雷诺数大的内流场，湍流粘度大，可能达到100的量级") 

        hydroDiameterLabel = QLabel("水力直径：")
        hydroDiameterLabel2 = QLabel("D=4A/L")
        hydroDiameterLabel.setToolTip("Hydraulic Diameter")   
        hydroDiameterLabel2.setToolTip("A为过流面积，L为湿周长度")   

        grid = QGridLayout()
        grid.addWidget(dynamicViscosityLabel, 0, 0)
        grid.addWidget(self.dynamicViscosityComboBox, 0, 1)

        grid.addWidget(densityLabel, 1, 0)
        grid.addWidget(self.densityComboBox, 1, 1)

        grid.addWidget(velocityLable, 2, 0)
        grid.addWidget(self.velocitySpinBox, 2, 1)

        grid.addWidget(lengthLable, 3, 0)
        grid.addWidget(self.lengthSpinBox, 3, 1)

        grid.addWidget(yPlusLable, 4, 0)
        grid.addWidget(self.yPlusSpinBox, 4, 1)

        grid.addWidget(ReLabel, 5, 0)
        grid.addWidget(self.ReLabel, 5, 1)

        grid.addWidget(CfLabel, 6, 0)
        grid.addWidget(self.CfLabel, 6, 1)

        grid.addWidget(tauLabel, 7, 0)
        grid.addWidget(self.tauLabel, 7, 1)

        grid.addWidget(U_tauLabel, 8, 0)
        grid.addWidget(self.U_tauLabel, 8, 1)

        grid.addWidget(yLabel, 9, 0)
        grid.addWidget(self.yLabel, 9, 1)  

        grid.addWidget(turbuIntensityLabel, 10, 0)
        grid.addWidget(self.turbuIntensityLabel, 10, 1)

        grid.addWidget(turbuLengthLabel, 11, 0)
        grid.addWidget(self.turbuLengthLabel, 11, 1)

        grid.addWidget(turbuKineticEnergyLabel, 12, 0)
        grid.addWidget(self.turbuKineticEnergyLabel, 12, 1)

        grid.addWidget(turbuDissipationLabel, 13, 0)
        grid.addWidget(self.turbuDissipationLabel, 13, 1)

        grid.addWidget(omegaLabel, 14, 0)
        grid.addWidget(self.omegaLabel, 14, 1)

        grid.addWidget(turbuViscosityRatioLabel, 15, 0)
        grid.addWidget(turbuViscosityRatioLabel2, 15, 1)

        grid.addWidget(hydroDiameterLabel, 16, 0)
        grid.addWidget(hydroDiameterLabel2, 16, 1)          

        self.setLayout(grid)

        self.dynamicViscosityComboBox.currentIndexChanged.connect(self.updateUi)
        self.velocitySpinBox.valueChanged.connect(self.updateUi)
        self.lengthSpinBox.valueChanged.connect(self.updateUi)
        self.yPlusSpinBox.valueChanged.connect(self.updateUi)

        self.setWindowTitle("yPlus By LiXia")
        self.updateUi()


    def updateUi(self):

        velocity = self.velocitySpinBox.value()
        length = self.lengthSpinBox.value()
        yPlus = self.yPlusSpinBox.value()

        self.densityComboBox.setCurrentIndex(self.dynamicViscosityComboBox.currentIndex())

        if self.dynamicViscosityComboBox.currentIndex():
            dynamicViscosity = 17.9*(10**-6)
        else:
            dynamicViscosity = 0.00101

        if self.densityComboBox.currentIndex():
            density = 1.293
        else:
            density = 998
        
        if velocity and length: # velocity or length cannot equal zero
            Re = density * velocity * length / dynamicViscosity
            Cf = 0.058 * Re ** -0.2
            tau_w = 0.5 * Cf * density * velocity ** 2
            U_tau = (tau_w/density) ** 0.5
            y = yPlus * dynamicViscosity / U_tau / density
            turbuIntensity = 0.16 * Re ** -0.125 *100 #按百分比显示
            turbuLength = 0.07 * length
            turbuKineticEnergy = 1.5 * (velocity * turbuIntensity) ** 2
            turbuDissipationRate = 0.1643167673 * (turbuKineticEnergy ** 1.5) / turbuLength
            omega = turbuKineticEnergy ** 0.5 /0.5477225575 / turbuLength 

            self.ReLabel.setText("%e"%Re)
            self.CfLabel.setText("%e"%Cf)
            self.tauLabel.setText("%e kg/(m·s^2)"%tau_w)
            self.U_tauLabel.setText("%e m/s"%U_tau)
            self.yLabel.setText("%e m"%y)
            self.yLabel.setStyleSheet("color:red") 
            self.turbuIntensityLabel.setText("%.2f%%"%turbuIntensity)
            self.turbuLengthLabel.setText("%e m"%turbuLength)
            self.turbuKineticEnergyLabel.setText("%e"%turbuKineticEnergy)
            self.turbuDissipationLabel.setText("%e"%turbuDissipationRate)
            self.omegaLabel.setText("%e"%omega)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
