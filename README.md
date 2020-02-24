# Machine Learning to Evaluate Robot Grasp Quality
A machine learning project to evaluate the robustness of a robotic gripper's grasp on a rigid spherical object, for the Course 11-663: Applied Machine Learning, at Carnegie Mellon University.

This project focuses on using machine learning to predict how well a robot arm grasps a rigid ball, in simulation. The dataset used is generated with the help of the smart grasping sandbox simulator, running on the open source platform ROS (Robot Operating System), and is available to use as a .csv file on kaggle.com. A screenshot of the simulator environment is shown below:

![Environment](/images/environment.jpg)

## Data Cleaning
The dataset contains 992,642 rows of data, where each row corresponds to one measurement. In order to aggregate the data such that for each experiment, we obtain only one row of feature values as the instance instead of multiple rows for each measurement, we must pre-process this data.

In order to do this, the data_cleaning_script first copies the first row containing the attribute names into a new .csv file. It also identifies which column corresponds to the measurement number attribute in the data. For all subsequent rows, the script adds up all feature values column-wise up until the measurement number resets to 0, signifying the start of a new set of measurements, i.e, the next experiment. When this happens, it then divides the sum of all feature values by the number of measurement rows it added up until that point. This finally gives us the average measurement values for all attributes, and the script then copies this row into the new file.

## Feature Engineering
One key aspect of this dataset, is that the relationship between attributes is a very important factor. Put in simple terms, even if one or two of the fingers move exactly the way they should to grasp the ball in the most optimal manner, the grip is still not going to be perfect unless the third finger does so as well. Hence, models that account for this relation are likely to perform far better. We can fix this problem for models which don't do so with the help of Feature Engineering. After determining through a preliminary analysis that the joint velocities and torques are problematic features, a new set of features was formulated, whose values are dependant on all joint velocities and torques. This engineering of the feature space then gave us a metric of the average joint velocities and torques of the
hand, which helped to predict the robustness better.

## Academic Integrity
If you are currently enrolled in the Graduate 16-782 Planning and Decision Making in Robotics, or the Undergraduate 16-350 Planning Techniques for Robotics course at Carnegie Mellon University, please refer to [CMUs Academic Integrity Policy](https://www.cmu.edu/policies/student-and-student-life/academic-integrity.html) before referring to any of the contents of this repository.