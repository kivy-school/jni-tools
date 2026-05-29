from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsoEra"]

class IsoEra(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/time/chrono/IsoEra"
    BCE = JavaStaticField("Ljava/time/chrono/IsoEra;")
    CE = JavaStaticField("Ljava/time/chrono/IsoEra;")
    values = JavaStaticMethod("()[Ljava/time/chrono/IsoEra;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/time/chrono/IsoEra;")
    of = JavaStaticMethod("(I)Ljava/time/chrono/IsoEra;")
    getValue = JavaMethod("()I")
    BCE = JavaStaticField("Ljava/time/chrono/IsoEra;")
    CE = JavaStaticField("Ljava/time/chrono/IsoEra;")