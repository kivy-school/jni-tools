from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrainingExamplesInput"]

class TrainingExamplesInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExamplesInput"
    getPopulationName = JavaMethod("()Ljava/lang/String;")
    getTaskName = JavaMethod("()Ljava/lang/String;")
    getResumptionToken = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")