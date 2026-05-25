from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Provider"]

class Provider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Provider"
    __javaconstructor__ = [("(Ljava/lang/String;DLjava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()D")
    getInfo = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    load = JavaMethod("(Ljava/io/InputStream;)V")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    entrySet = JavaMethod("()Ljava/util/Set;")
    keySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    remove = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Z", False, False)])
    replace = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    compute = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    computeIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/Function;)Ljava/lang/Object;")
    computeIfPresent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    merge = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    getOrDefault = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    keys = JavaMethod("()Ljava/util/Enumeration;")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getService = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/Provider$Service;")
    getServices = JavaMethod("()Ljava/util/Set;")
    putService = JavaMethod("(Ljava/security/Provider$Service;)V")
    removeService = JavaMethod("(Ljava/security/Provider$Service;)V")

    class Service(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/Provider/Service"
        __javaconstructor__ = [("(Ljava/security/Provider;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/List;Ljava/util/Map;)V", False)]
        getType = JavaMethod("()Ljava/lang/String;")
        getAlgorithm = JavaMethod("()Ljava/lang/String;")
        getProvider = JavaMethod("()Ljava/security/Provider;")
        getClassName = JavaMethod("()Ljava/lang/String;")
        getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
        newInstance = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
        supportsParameter = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")