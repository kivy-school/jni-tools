from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PersistentDataBlockManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/persistentdata/PersistentDataBlockManager"
    isFactoryResetProtectionActive = JavaMethod("()Z")