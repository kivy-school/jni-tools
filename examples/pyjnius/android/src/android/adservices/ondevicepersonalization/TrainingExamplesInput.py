from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrainingExamplesInput"]

class TrainingExamplesInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExamplesInput"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;[BLjava/lang/String;)V", False)]
    getCollectionName = JavaMethod("()Ljava/lang/String;")
    getResumptionToken = JavaMethod("()[B")
    getPopulationName = JavaMethod("()Ljava/lang/String;")
    getTaskName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")