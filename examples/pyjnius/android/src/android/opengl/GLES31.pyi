from typing import Any, ClassVar, overload
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES31:
    GL_ACTIVE_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_ACTIVE_PROGRAM: ClassVar[int]
    GL_ACTIVE_RESOURCES: ClassVar[int]
    GL_ACTIVE_VARIABLES: ClassVar[int]
    GL_ALL_BARRIER_BITS: ClassVar[int]
    GL_ALL_SHADER_BITS: ClassVar[int]
    GL_ARRAY_SIZE: ClassVar[int]
    GL_ARRAY_STRIDE: ClassVar[int]
    GL_ATOMIC_COUNTER_BARRIER_BIT: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_BINDING: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_INDEX: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_SIZE: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_START: ClassVar[int]
    GL_BLOCK_INDEX: ClassVar[int]
    GL_BUFFER_BINDING: ClassVar[int]
    GL_BUFFER_DATA_SIZE: ClassVar[int]
    GL_BUFFER_UPDATE_BARRIER_BIT: ClassVar[int]
    GL_BUFFER_VARIABLE: ClassVar[int]
    GL_COMMAND_BARRIER_BIT: ClassVar[int]
    GL_COMPUTE_SHADER: ClassVar[int]
    GL_COMPUTE_SHADER_BIT: ClassVar[int]
    GL_COMPUTE_WORK_GROUP_SIZE: ClassVar[int]
    GL_DEPTH_STENCIL_TEXTURE_MODE: ClassVar[int]
    GL_DISPATCH_INDIRECT_BUFFER: ClassVar[int]
    GL_DISPATCH_INDIRECT_BUFFER_BINDING: ClassVar[int]
    GL_DRAW_INDIRECT_BUFFER: ClassVar[int]
    GL_DRAW_INDIRECT_BUFFER_BINDING: ClassVar[int]
    GL_ELEMENT_ARRAY_BARRIER_BIT: ClassVar[int]
    GL_FRAGMENT_SHADER_BIT: ClassVar[int]
    GL_FRAMEBUFFER_BARRIER_BIT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_HEIGHT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_SAMPLES: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_WIDTH: ClassVar[int]
    GL_IMAGE_2D: ClassVar[int]
    GL_IMAGE_2D_ARRAY: ClassVar[int]
    GL_IMAGE_3D: ClassVar[int]
    GL_IMAGE_BINDING_ACCESS: ClassVar[int]
    GL_IMAGE_BINDING_FORMAT: ClassVar[int]
    GL_IMAGE_BINDING_LAYER: ClassVar[int]
    GL_IMAGE_BINDING_LAYERED: ClassVar[int]
    GL_IMAGE_BINDING_LEVEL: ClassVar[int]
    GL_IMAGE_BINDING_NAME: ClassVar[int]
    GL_IMAGE_CUBE: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_TYPE: ClassVar[int]
    GL_INT_IMAGE_2D: ClassVar[int]
    GL_INT_IMAGE_2D_ARRAY: ClassVar[int]
    GL_INT_IMAGE_3D: ClassVar[int]
    GL_INT_IMAGE_CUBE: ClassVar[int]
    GL_INT_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_IS_ROW_MAJOR: ClassVar[int]
    GL_LOCATION: ClassVar[int]
    GL_MATRIX_STRIDE: ClassVar[int]
    GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE: ClassVar[int]
    GL_MAX_COLOR_TEXTURE_SAMPLES: ClassVar[int]
    GL_MAX_COMBINED_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES: ClassVar[int]
    GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_COMPUTE_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_SHARED_MEMORY_SIZE: ClassVar[int]
    GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_COMPUTE_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_COUNT: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_SIZE: ClassVar[int]
    GL_MAX_DEPTH_TEXTURE_SAMPLES: ClassVar[int]
    GL_MAX_FRAGMENT_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_FRAGMENT_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_FRAMEBUFFER_HEIGHT: ClassVar[int]
    GL_MAX_FRAMEBUFFER_SAMPLES: ClassVar[int]
    GL_MAX_FRAMEBUFFER_WIDTH: ClassVar[int]
    GL_MAX_IMAGE_UNITS: ClassVar[int]
    GL_MAX_INTEGER_SAMPLES: ClassVar[int]
    GL_MAX_NAME_LENGTH: ClassVar[int]
    GL_MAX_NUM_ACTIVE_VARIABLES: ClassVar[int]
    GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET: ClassVar[int]
    GL_MAX_SAMPLE_MASK_WORDS: ClassVar[int]
    GL_MAX_SHADER_STORAGE_BLOCK_SIZE: ClassVar[int]
    GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_UNIFORM_LOCATIONS: ClassVar[int]
    GL_MAX_VERTEX_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_BINDINGS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_STRIDE: ClassVar[int]
    GL_MAX_VERTEX_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET: ClassVar[int]
    GL_NAME_LENGTH: ClassVar[int]
    GL_NUM_ACTIVE_VARIABLES: ClassVar[int]
    GL_OFFSET: ClassVar[int]
    GL_PIXEL_BUFFER_BARRIER_BIT: ClassVar[int]
    GL_PROGRAM_INPUT: ClassVar[int]
    GL_PROGRAM_OUTPUT: ClassVar[int]
    GL_PROGRAM_PIPELINE_BINDING: ClassVar[int]
    GL_PROGRAM_SEPARABLE: ClassVar[int]
    GL_READ_ONLY: ClassVar[int]
    GL_READ_WRITE: ClassVar[int]
    GL_REFERENCED_BY_COMPUTE_SHADER: ClassVar[int]
    GL_REFERENCED_BY_FRAGMENT_SHADER: ClassVar[int]
    GL_REFERENCED_BY_VERTEX_SHADER: ClassVar[int]
    GL_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_SAMPLE_MASK: ClassVar[int]
    GL_SAMPLE_MASK_VALUE: ClassVar[int]
    GL_SAMPLE_POSITION: ClassVar[int]
    GL_SHADER_IMAGE_ACCESS_BARRIER_BIT: ClassVar[int]
    GL_SHADER_STORAGE_BARRIER_BIT: ClassVar[int]
    GL_SHADER_STORAGE_BLOCK: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_BINDING: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_SIZE: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_START: ClassVar[int]
    GL_STENCIL_INDEX: ClassVar[int]
    GL_TEXTURE_2D_MULTISAMPLE: ClassVar[int]
    GL_TEXTURE_ALPHA_SIZE: ClassVar[int]
    GL_TEXTURE_ALPHA_TYPE: ClassVar[int]
    GL_TEXTURE_BINDING_2D_MULTISAMPLE: ClassVar[int]
    GL_TEXTURE_BLUE_SIZE: ClassVar[int]
    GL_TEXTURE_BLUE_TYPE: ClassVar[int]
    GL_TEXTURE_COMPRESSED: ClassVar[int]
    GL_TEXTURE_DEPTH: ClassVar[int]
    GL_TEXTURE_DEPTH_SIZE: ClassVar[int]
    GL_TEXTURE_DEPTH_TYPE: ClassVar[int]
    GL_TEXTURE_FETCH_BARRIER_BIT: ClassVar[int]
    GL_TEXTURE_FIXED_SAMPLE_LOCATIONS: ClassVar[int]
    GL_TEXTURE_GREEN_SIZE: ClassVar[int]
    GL_TEXTURE_GREEN_TYPE: ClassVar[int]
    GL_TEXTURE_HEIGHT: ClassVar[int]
    GL_TEXTURE_INTERNAL_FORMAT: ClassVar[int]
    GL_TEXTURE_RED_SIZE: ClassVar[int]
    GL_TEXTURE_RED_TYPE: ClassVar[int]
    GL_TEXTURE_SAMPLES: ClassVar[int]
    GL_TEXTURE_SHARED_SIZE: ClassVar[int]
    GL_TEXTURE_STENCIL_SIZE: ClassVar[int]
    GL_TEXTURE_UPDATE_BARRIER_BIT: ClassVar[int]
    GL_TEXTURE_WIDTH: ClassVar[int]
    GL_TOP_LEVEL_ARRAY_SIZE: ClassVar[int]
    GL_TOP_LEVEL_ARRAY_STRIDE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BARRIER_BIT: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYING: ClassVar[int]
    GL_TYPE: ClassVar[int]
    GL_UNIFORM: ClassVar[int]
    GL_UNIFORM_BARRIER_BIT: ClassVar[int]
    GL_UNIFORM_BLOCK: ClassVar[int]
    GL_UNSIGNED_INT_ATOMIC_COUNTER: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_2D: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_2D_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_3D: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_CUBE: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT: ClassVar[int]
    GL_VERTEX_ATTRIB_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_RELATIVE_OFFSET: ClassVar[int]
    GL_VERTEX_BINDING_BUFFER: ClassVar[int]
    GL_VERTEX_BINDING_DIVISOR: ClassVar[int]
    GL_VERTEX_BINDING_OFFSET: ClassVar[int]
    GL_VERTEX_BINDING_STRIDE: ClassVar[int]
    GL_VERTEX_SHADER_BIT: ClassVar[int]
    GL_WRITE_ONLY: ClassVar[int]
    @staticmethod
    def glDispatchCompute(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glDispatchComputeIndirect(arg0: int) -> None: ...
    @staticmethod
    def glDrawArraysIndirect(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glDrawElementsIndirect(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glFramebufferParameteri(arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferParameteriv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferParameteriv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramInterfaceiv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramInterfaceiv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @staticmethod
    def glGetProgramResourceIndex(arg0: int, arg1: int, arg2: str) -> int: ...
    @staticmethod
    def glGetProgramResourceName(arg0: int, arg1: int, arg2: int) -> str: ...
    @overload
    @staticmethod
    def glGetProgramResourceiv(arg0: int, arg1: int, arg2: int, arg3: int, arg4: list[int], arg5: int, arg6: int, arg7: list[int], arg8: int, arg9: list[int], arg10: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramResourceiv(arg0: int, arg1: int, arg2: int, arg3: int, arg4: IntBuffer, arg5: int, arg6: IntBuffer, arg7: IntBuffer) -> None: ...
    @staticmethod
    def glGetProgramResourceLocation(arg0: int, arg1: int, arg2: str) -> int: ...
    @staticmethod
    def glUseProgramStages(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glActiveShaderProgram(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glCreateShaderProgramv(arg0: int, arg1: list[str]) -> int: ...
    @staticmethod
    def glBindProgramPipeline(arg0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteProgramPipelines(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteProgramPipelines(arg0: int, arg1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenProgramPipelines(arg0: int, arg1: list[int], arg2: int) -> None: ...
    @overload
    @staticmethod
    def glGenProgramPipelines(arg0: int, arg1: IntBuffer) -> None: ...
    @staticmethod
    def glIsProgramPipeline(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def glGetProgramPipelineiv(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramPipelineiv(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glProgramUniform1i(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glProgramUniform2i(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glProgramUniform3i(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glProgramUniform4i(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @staticmethod
    def glProgramUniform1ui(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glProgramUniform2ui(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glProgramUniform3ui(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glProgramUniform4ui(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    @staticmethod
    def glProgramUniform1f(arg0: int, arg1: int, arg2: float) -> None: ...
    @staticmethod
    def glProgramUniform2f(arg0: int, arg1: int, arg2: float, arg3: float) -> None: ...
    @staticmethod
    def glProgramUniform3f(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float) -> None: ...
    @staticmethod
    def glProgramUniform4f(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1iv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1iv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2iv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2iv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3iv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3iv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4iv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4iv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1uiv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1uiv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2uiv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2uiv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3uiv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3uiv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4uiv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4uiv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1fv(arg0: int, arg1: int, arg2: int, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1fv(arg0: int, arg1: int, arg2: int, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2fv(arg0: int, arg1: int, arg2: int, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2fv(arg0: int, arg1: int, arg2: int, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3fv(arg0: int, arg1: int, arg2: int, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3fv(arg0: int, arg1: int, arg2: int, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4fv(arg0: int, arg1: int, arg2: int, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4fv(arg0: int, arg1: int, arg2: int, arg3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x3fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x3fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x2fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x2fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x4fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x4fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x2fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x2fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x4fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x4fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x3fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list[float], arg5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x3fv(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: FloatBuffer) -> None: ...
    @staticmethod
    def glValidateProgramPipeline(arg0: int) -> None: ...
    @staticmethod
    def glGetProgramPipelineInfoLog(arg0: int) -> str: ...
    @staticmethod
    def glBindImageTexture(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int) -> None: ...
    @overload
    @staticmethod
    def glGetBooleani_v(arg0: int, arg1: int, arg2: list[bool], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetBooleani_v(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glMemoryBarrier(arg0: int) -> None: ...
    @staticmethod
    def glMemoryBarrierByRegion(arg0: int) -> None: ...
    @staticmethod
    def glTexStorage2DMultisample(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool) -> None: ...
    @overload
    @staticmethod
    def glGetMultisamplefv(arg0: int, arg1: int, arg2: list[float], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetMultisamplefv(arg0: int, arg1: int, arg2: FloatBuffer) -> None: ...
    @staticmethod
    def glSampleMaski(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameteriv(arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameteriv(arg0: int, arg1: int, arg2: int, arg3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameterfv(arg0: int, arg1: int, arg2: int, arg3: list[float], arg4: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameterfv(arg0: int, arg1: int, arg2: int, arg3: FloatBuffer) -> None: ...
    @staticmethod
    def glBindVertexBuffer(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glVertexAttribFormat(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int) -> None: ...
    @staticmethod
    def glVertexAttribIFormat(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glVertexAttribBinding(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glVertexBindingDivisor(arg0: int, arg1: int) -> None: ...
