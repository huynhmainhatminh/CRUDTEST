
using CRUDDATABASE.DAL;

namespace CRUDDATABASE.Repository.Implementations
{
    public class UnitOfWork : IUnitOfWork
    {
        private readonly ApptvcakoiContext _apptvcakoiContext;

        public IUserRepository userRepository { get; private set; }


        public UnitOfWork(ApptvcakoiContext apptvcakoiContext)
        {
            _apptvcakoiContext = apptvcakoiContext;
            userRepository = new UserRepository(_apptvcakoiContext);
        }


        public async Task<int> SaveASync()
        {
            return await _apptvcakoiContext.SaveChangesAsync();
        }
    }
}
