from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Pack200"]

class Pack200(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/jar/Pack200"
    newPacker = JavaStaticMethod("()Ljava/util/jar/Pack200$Packer;")
    newUnpacker = JavaStaticMethod("()Ljava/util/jar/Pack200$Unpacker;")

    class Packer(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/jar/Pack200/Packer"
        CLASS_ATTRIBUTE_PFX = JavaStaticField("Ljava/lang/String;")
        CODE_ATTRIBUTE_PFX = JavaStaticField("Ljava/lang/String;")
        DEFLATE_HINT = JavaStaticField("Ljava/lang/String;")
        EFFORT = JavaStaticField("Ljava/lang/String;")
        ERROR = JavaStaticField("Ljava/lang/String;")
        FALSE = JavaStaticField("Ljava/lang/String;")
        FIELD_ATTRIBUTE_PFX = JavaStaticField("Ljava/lang/String;")
        KEEP = JavaStaticField("Ljava/lang/String;")
        KEEP_FILE_ORDER = JavaStaticField("Ljava/lang/String;")
        LATEST = JavaStaticField("Ljava/lang/String;")
        METHOD_ATTRIBUTE_PFX = JavaStaticField("Ljava/lang/String;")
        MODIFICATION_TIME = JavaStaticField("Ljava/lang/String;")
        PASS = JavaStaticField("Ljava/lang/String;")
        PASS_FILE_PFX = JavaStaticField("Ljava/lang/String;")
        PROGRESS = JavaStaticField("Ljava/lang/String;")
        SEGMENT_LIMIT = JavaStaticField("Ljava/lang/String;")
        STRIP = JavaStaticField("Ljava/lang/String;")
        TRUE = JavaStaticField("Ljava/lang/String;")
        UNKNOWN_ATTRIBUTE = JavaStaticField("Ljava/lang/String;")
        properties = JavaMethod("()Ljava/util/SortedMap;")
        pack = JavaMultipleMethod([("(Ljava/util/jar/JarFile;Ljava/io/OutputStream;)V", False, False), ("(Ljava/util/jar/JarInputStream;Ljava/io/OutputStream;)V", False, False)])
        addPropertyChangeListener = JavaMethod("(Ljava/beans/PropertyChangeListener;)V")
        removePropertyChangeListener = JavaMethod("(Ljava/beans/PropertyChangeListener;)V")

    class Unpacker(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/jar/Pack200/Unpacker"
        DEFLATE_HINT = JavaStaticField("Ljava/lang/String;")
        FALSE = JavaStaticField("Ljava/lang/String;")
        KEEP = JavaStaticField("Ljava/lang/String;")
        PROGRESS = JavaStaticField("Ljava/lang/String;")
        TRUE = JavaStaticField("Ljava/lang/String;")
        properties = JavaMethod("()Ljava/util/SortedMap;")
        unpack = JavaMultipleMethod([("(Ljava/io/InputStream;Ljava/util/jar/JarOutputStream;)V", False, False), ("(Ljava/io/File;Ljava/util/jar/JarOutputStream;)V", False, False)])
        addPropertyChangeListener = JavaMethod("(Ljava/beans/PropertyChangeListener;)V")
        removePropertyChangeListener = JavaMethod("(Ljava/beans/PropertyChangeListener;)V")