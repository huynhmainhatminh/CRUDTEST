namespace CRUDDATABASE.Repository
{
    public interface IUnitOfWork
    {
        IUserRepository userRepository { get; }
        Task<int> SaveASync();
    }
}
