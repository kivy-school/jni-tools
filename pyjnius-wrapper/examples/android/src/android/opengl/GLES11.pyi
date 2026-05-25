from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES11:
    GL_ACTIVE_TEXTURE: ClassVar[int]
    GL_ADD_SIGNED: ClassVar[int]
    GL_ALPHA_SCALE: ClassVar[int]
    GL_ALPHA_TEST_FUNC: ClassVar[int]
    GL_ALPHA_TEST_REF: ClassVar[int]
    GL_ARRAY_BUFFER: ClassVar[int]
    GL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_BLEND_DST: ClassVar[int]
    GL_BLEND_SRC: ClassVar[int]
    GL_BUFFER_ACCESS: ClassVar[int]
    GL_BUFFER_SIZE: ClassVar[int]
    GL_BUFFER_USAGE: ClassVar[int]
    GL_CLIENT_ACTIVE_TEXTURE: ClassVar[int]
    GL_CLIP_PLANE0: ClassVar[int]
    GL_CLIP_PLANE1: ClassVar[int]
    GL_CLIP_PLANE2: ClassVar[int]
    GL_CLIP_PLANE3: ClassVar[int]
    GL_CLIP_PLANE4: ClassVar[int]
    GL_CLIP_PLANE5: ClassVar[int]
    GL_COLOR_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_COLOR_ARRAY_POINTER: ClassVar[int]
    GL_COLOR_ARRAY_SIZE: ClassVar[int]
    GL_COLOR_ARRAY_STRIDE: ClassVar[int]
    GL_COLOR_ARRAY_TYPE: ClassVar[int]
    GL_COLOR_CLEAR_VALUE: ClassVar[int]
    GL_COLOR_WRITEMASK: ClassVar[int]
    GL_COMBINE: ClassVar[int]
    GL_COMBINE_ALPHA: ClassVar[int]
    GL_COMBINE_RGB: ClassVar[int]
    GL_CONSTANT: ClassVar[int]
    GL_COORD_REPLACE_OES: ClassVar[int]
    GL_CULL_FACE_MODE: ClassVar[int]
    GL_CURRENT_COLOR: ClassVar[int]
    GL_CURRENT_NORMAL: ClassVar[int]
    GL_CURRENT_TEXTURE_COORDS: ClassVar[int]
    GL_DEPTH_CLEAR_VALUE: ClassVar[int]
    GL_DEPTH_FUNC: ClassVar[int]
    GL_DEPTH_RANGE: ClassVar[int]
    GL_DEPTH_WRITEMASK: ClassVar[int]
    GL_DOT3_RGB: ClassVar[int]
    GL_DOT3_RGBA: ClassVar[int]
    GL_DYNAMIC_DRAW: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_FRONT_FACE: ClassVar[int]
    GL_GENERATE_MIPMAP: ClassVar[int]
    GL_GENERATE_MIPMAP_HINT: ClassVar[int]
    GL_INTERPOLATE: ClassVar[int]
    GL_LINE_WIDTH: ClassVar[int]
    GL_LOGIC_OP_MODE: ClassVar[int]
    GL_MATRIX_MODE: ClassVar[int]
    GL_MAX_CLIP_PLANES: ClassVar[int]
    GL_MODELVIEW_MATRIX: ClassVar[int]
    GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_MODELVIEW_STACK_DEPTH: ClassVar[int]
    GL_NORMAL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_NORMAL_ARRAY_POINTER: ClassVar[int]
    GL_NORMAL_ARRAY_STRIDE: ClassVar[int]
    GL_NORMAL_ARRAY_TYPE: ClassVar[int]
    GL_OPERAND0_ALPHA: ClassVar[int]
    GL_OPERAND0_RGB: ClassVar[int]
    GL_OPERAND1_ALPHA: ClassVar[int]
    GL_OPERAND1_RGB: ClassVar[int]
    GL_OPERAND2_ALPHA: ClassVar[int]
    GL_OPERAND2_RGB: ClassVar[int]
    GL_POINT_DISTANCE_ATTENUATION: ClassVar[int]
    GL_POINT_FADE_THRESHOLD_SIZE: ClassVar[int]
    GL_POINT_SIZE: ClassVar[int]
    GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_POINTER_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_STRIDE_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_TYPE_OES: ClassVar[int]
    GL_POINT_SIZE_MAX: ClassVar[int]
    GL_POINT_SIZE_MIN: ClassVar[int]
    GL_POINT_SPRITE_OES: ClassVar[int]
    GL_POLYGON_OFFSET_FACTOR: ClassVar[int]
    GL_POLYGON_OFFSET_UNITS: ClassVar[int]
    GL_PREVIOUS: ClassVar[int]
    GL_PRIMARY_COLOR: ClassVar[int]
    GL_PROJECTION_MATRIX: ClassVar[int]
    GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_PROJECTION_STACK_DEPTH: ClassVar[int]
    GL_RGB_SCALE: ClassVar[int]
    GL_SAMPLES: ClassVar[int]
    GL_SAMPLE_BUFFERS: ClassVar[int]
    GL_SAMPLE_COVERAGE_INVERT: ClassVar[int]
    GL_SAMPLE_COVERAGE_VALUE: ClassVar[int]
    GL_SCISSOR_BOX: ClassVar[int]
    GL_SHADE_MODEL: ClassVar[int]
    GL_SRC0_ALPHA: ClassVar[int]
    GL_SRC0_RGB: ClassVar[int]
    GL_SRC1_ALPHA: ClassVar[int]
    GL_SRC1_RGB: ClassVar[int]
    GL_SRC2_ALPHA: ClassVar[int]
    GL_SRC2_RGB: ClassVar[int]
    GL_STATIC_DRAW: ClassVar[int]
    GL_STENCIL_CLEAR_VALUE: ClassVar[int]
    GL_STENCIL_FAIL: ClassVar[int]
    GL_STENCIL_FUNC: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_REF: ClassVar[int]
    GL_STENCIL_VALUE_MASK: ClassVar[int]
    GL_STENCIL_WRITEMASK: ClassVar[int]
    GL_SUBTRACT: ClassVar[int]
    GL_TEXTURE_BINDING_2D: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_POINTER: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_SIZE: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_STRIDE: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_TYPE: ClassVar[int]
    GL_TEXTURE_MATRIX: ClassVar[int]
    GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_TEXTURE_STACK_DEPTH: ClassVar[int]
    GL_VERTEX_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_VERTEX_ARRAY_POINTER: ClassVar[int]
    GL_VERTEX_ARRAY_SIZE: ClassVar[int]
    GL_VERTEX_ARRAY_STRIDE: ClassVar[int]
    GL_VERTEX_ARRAY_TYPE: ClassVar[int]
    GL_VIEWPORT: ClassVar[int]
    GL_WRITE_ONLY: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glBindBuffer(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBufferData(arg0: int, arg1: int, arg2: Buffer, arg3: int) -> None: ...
    @staticmethod
    def glBufferSubData(arg0: int, arg1: int, arg2: int, arg3: Buffer) -> None: ...
    @overload
    @staticmethod
    def glClipPlanef(arg0: int, arg1: list[float], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanef(arg0: int, arg1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glClipPlanex(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanex(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glColor4ub(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glColorPointer(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteBuffers(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteBuffers(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glDrawElements(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGenBuffers(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenBuffers(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBooleanv(arg0: int, arg1: list[bool], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetBooleanv(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteriv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteriv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanef(arg0: int, arg1: list[float], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanef(arg0: int, arg1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanex(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanex(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFixedv(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFixedv(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFloatv(arg0: int, arg1: list[float], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFloatv(arg0: int, arg1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetLightfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetLightfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetLightxv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetLightxv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnviv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnviv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameteriv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameteriv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glIsBuffer(arg0: int) -> bool: ...
    @staticmethod
    def glIsEnabled(arg0: int) -> bool: ...
    @staticmethod
    def glIsTexture(arg0: int) -> bool: ...
    @staticmethod
    def glNormalPointer(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glPointParameterf(arg0: int, arg1: float) -> None: ...
    @overload
    @staticmethod
    def glPointParameterfv(arg0: int, arg1: list[float], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterfv(arg0: int, arg1: FloatBuffer) -> None: ...
    @staticmethod
    def glPointParameterx(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxv(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxv(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glPointSizePointerOES(arg0: int, arg1: int, arg2: Buffer) -> None: ...
    @staticmethod
    def glTexCoordPointer(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glTexEnvi(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnviv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnviv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameterfv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterfv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @staticmethod
    def glTexParameteri(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameteriv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameteriv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glVertexPointer(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
