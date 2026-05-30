from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IndexedPropertyChangeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/IndexedPropertyChangeEvent"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;I)V", False)]
    getIndex = JavaMethod("()I")

class PropertyChangeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeEvent"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V", False)]
    getNewValue = JavaMethod("()Ljava/lang/Object;")
    getOldValue = JavaMethod("()Ljava/lang/Object;")
    getPropagationId = JavaMethod("()Ljava/lang/Object;")
    setPropagationId = JavaMethod("(Ljava/lang/Object;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getPropertyName = JavaMethod("()Ljava/lang/String;")

class PropertyChangeSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeSupport"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False)]
    addPropertyChangeListener = JavaMultipleMethod([("(Ljava/lang/String;Ljava/beans/PropertyChangeListener;)V", False, False), ("(Ljava/beans/PropertyChangeListener;)V", False, False)])
    removePropertyChangeListener = JavaMultipleMethod([("(Ljava/lang/String;Ljava/beans/PropertyChangeListener;)V", False, False), ("(Ljava/beans/PropertyChangeListener;)V", False, False)])
    firePropertyChange = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V", False, False), ("(Ljava/lang/String;II)V", False, False), ("(Ljava/beans/PropertyChangeEvent;)V", False, False), ("(Ljava/lang/String;ZZ)V", False, False)])
    fireIndexedPropertyChange = JavaMultipleMethod([("(Ljava/lang/String;IZZ)V", False, False), ("(Ljava/lang/String;ILjava/lang/Object;Ljava/lang/Object;)V", False, False), ("(Ljava/lang/String;III)V", False, False)])
    hasListeners = JavaMethod("(Ljava/lang/String;)Z")
    getPropertyChangeListeners = JavaMultipleMethod([("()[Ljava/beans/PropertyChangeListener;", False, False), ("(Ljava/lang/String;)[Ljava/beans/PropertyChangeListener;", False, False)])

class PropertyChangeListenerProxy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeListenerProxy"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/beans/PropertyChangeListener;)V", False)]
    propertyChange = JavaMethod("(Ljava/beans/PropertyChangeEvent;)V")
    getPropertyName = JavaMethod("()Ljava/lang/String;")

class PropertyChangeListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeListener"
    propertyChange = JavaMethod("(Ljava/beans/PropertyChangeEvent;)V")