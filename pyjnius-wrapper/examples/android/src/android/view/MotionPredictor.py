from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MotionPredictor"]

class MotionPredictor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/MotionPredictor"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    record = JavaMethod("(Landroid/view/MotionEvent;)V")
    predict = JavaMethod("(J)Landroid/view/MotionEvent;")
    isPredictionAvailable = JavaMethod("(II)Z")