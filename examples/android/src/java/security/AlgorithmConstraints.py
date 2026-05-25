from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmConstraints"]

class AlgorithmConstraints(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmConstraints"
    permits = JavaMultipleMethod([("(Ljava/util/Set;Ljava/lang/String;Ljava/security/AlgorithmParameters;)Z", False, False), ("(Ljava/util/Set;Ljava/security/Key;)Z", False, False), ("(Ljava/util/Set;Ljava/lang/String;Ljava/security/Key;Ljava/security/AlgorithmParameters;)Z", False, False)])