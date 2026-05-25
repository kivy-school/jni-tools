from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FragmentManagerNonConfig"]

class FragmentManagerNonConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/FragmentManagerNonConfig"